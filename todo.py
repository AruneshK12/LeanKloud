from flask import Flask,request
from flask_restplus import Api, Resource, fields
from werkzeug.middleware.proxy_fix import ProxyFix
from functools import wraps
import mysql.connector

mydb=mysql.connector.connect(host="localhost",username="root",password="ADMIN",database="test")


auth_types={
    'AccessKey':{
        'type':'apiKey',
        'in':'header',
        'name':'Task-Key'
    }
}
app = Flask(__name__)

app.wsgi_app = ProxyFix(app.wsgi_app)
api = Api(app, version='1.0', title='TodoMVC API',description='A simple TodoMVC API',authorizations=auth_types)

def token_required_write(f):
    @wraps(f)
    def decorated(*args,**kwargs):
        token= None
        check=0
        if 'Task-Key' in request.headers:
            token=request.headers['Task-Key']
            myc2=mydb.cursor()
            query="Select * from AcessKeys where KeyName=\""+str(token)+"\""
            myc2.execute(query)
            token_det=myc2.fetchall()
            for row in token_det:
                check=1
                if(row[1]==0):
                    return {'message':'Invalid Write-Key, Operation Denied'},401
        if(check==0):
            return {'message':'Access Key Doesnt Exist, Operation Deined'},401
        if not token:
            return {'message':'Missing Access Key,Operation Terminated'},401
        return f(*args,**kwargs)
    return decorated

def token_required_read(f):
    @wraps(f)
    def decorated(*args,**kwargs):
        token= None
        check=0
        if 'Task-Key' in request.headers:
            token=request.headers['Task-Key']
            myc2=mydb.cursor()
            query="Select * from AcessKeys where KeyName=\""+str(token)+"\""
            myc2.execute(query)
            token_det=myc2.fetchall()
            for row in token_det:
                check=1
                if(row[1]==1):
                    return {'message':'Invalid Read-Key, Operation Denied'},401
        if(check==0):
            return {'message':'Access Key Doesnt Exist, Operation Deined'},401
        if not token:
            return {'message':'Missing Access Key,Operation Terminated'},401
        return f(*args,**kwargs)
    return decorated

ns = api.namespace('todos', description='TODO operations')

todo = api.model('Todo', {
    'id': fields.Integer(readonly=True, description='The task unique identifier'),
    'task': fields.String(required=True, description='The task details'),
    'due by': fields.String(required=True, description='The due date of task in YYYY-MM-DD format'),
    'Status': fields.String(required=True, description="Current status of task")
})

todo_status=api.model('Todo_status',{
    'Status': fields.String(required=True,description="Current Status of task")
})

todo_task=api.model('Todo_Task',{
    'task': fields.String(required=True,description="The task details")
})
class TodoDAO(object):
    def __init__(self):
        self.counter = 0
        self.todos = []
    def getAll(self):
        myc2=mydb.cursor()
        myc2.execute("SELECT * FROM todoList")
        all_todos=myc2.fetchall()
        todo_list=[]
        for row in all_todos:
            temp={}
            temp['id'],temp['task'],temp['due by'],temp['Status']=row[0],row[1],row[2],row[3]
            todo_list.append(temp)
        return todo_list
    def get(self, id):
        myc2=mydb.cursor()
        query="SELECT * FROM todoList WHERE id="+str(id)
        myc2.execute(query)
        todo_id=myc2.fetchall()
        todo_dict={}
        for row in todo_id:
            todo_dict["id"],todo_dict["task"],todo_dict['due by'],todo_dict['Status']=row[0],row[1],row[2],row[3]
            return todo_dict
        api.abort(404, "Todo {} doesn't exist".format(id))

    def create(self, data):
        myc2=mydb.cursor()
        myc2.execute("SELECT COUNT(*) FROM todoList")
        todo_id=myc2.fetchall()
        counter=todo_id[0][0]
        todo = data
        task=data['task']
        dueBy=data['due by']
        status=data['Status']
        myc1=mydb.cursor()
        query="INSERT INTO todoList(task,Dueby,Status) values (%s,%s,%s)"
        val=(task,dueBy,status)
        myc1.execute(query,val)
        mydb.commit()
        todo['id'] = counter + 1
        #self.todos.append(todo)
        return todo

    def updateStatus(self, id, stat):
        myc1=mydb.cursor()
        status=stat['Status']
        query="UPDATE todoList set Status=%s where id="+str(id)
        val=(status,)
        myc1.execute(query,val)
        mydb.commit()
        myc2=mydb.cursor()
        query="SELECT * FROM todoList WHERE id="+str(id)
        myc2.execute(query)
        todo_id=myc2.fetchall()
        todo_dict={}
        for row in todo_id:
            todo_dict["id"],todo_dict["task"],todo_dict['due by'],todo_dict['Status']=row[0],row[1],row[2],row[3]
            return todo_dict

    def update(self, id, data):
        task=data['task']
        myc1=mydb.cursor()
        query="UPDATE todoList set task=%s where id="+str(id)
        val=(task,)
        myc1.execute(query,val)
        mydb.commit()
        myc2=mydb.cursor()
        query="SELECT * FROM todoList WHERE id="+str(id)
        myc2.execute(query)
        todo_id=myc2.fetchall()
        todo_dict={}
        for row in todo_id:
            todo_dict["id"],todo_dict["task"],todo_dict['due by'],todo_dict['Status']=row[0],row[1],row[2],row[3]
            return todo_dict

    def delete(self, id):
        myc1=mydb.cursor()
        query="DELETE FROM todoList where id="+str(id)
        myc1.execute(query)
        mydb.commit()

    def tasksTobeFinished(self,data):
        myc1=mydb.cursor()
        due_date=data
        query="select * from todoList where DueBy<="+due_date+" and Status!=\"Finished\""
        myc1.execute(query)
        todo_query=myc1.fetchall()
        todo_dict=[]
        for row in todo_query:
            temp={}
            temp["id"],temp["task"],temp['due by'],temp['Status']=str(row[0]),str(row[1]),str(row[2]),str(row[3])
            todo_dict.append(temp)
        return todo_dict
    
    def overdueTasks(self):
        myc2=mydb.cursor()
        query="select * from todoList where DueBy<(select curdate()) and Status!=\"Finished\""
        myc2.execute(query)
        todo_query=myc2.fetchall()
        todo_dict=[]
        for row in todo_query:
            temp={}
            temp["id"],temp["task"],temp['due by'],temp['Status']=str(row[0]),str(row[1]),str(row[2]),str(row[3])
            todo_dict.append(temp)
        if(todo_dict==[]):
            return ["EMPTY"]
        return todo_dict
    
    def finished(self):
        myc2=mydb.cursor()
        query="select * from todoList where Status=\"Finished\""
        myc2.execute(query)
        todo_query=myc2.fetchall()
        todo_dict=[]
        for row in todo_query:
            temp={}
            temp["id"],temp["task"],temp['due by'],temp['Status']=str(row[0]),str(row[1]),str(row[2]),str(row[3])
            todo_dict.append(temp)
        if(todo_dict==[]):
            return ["EMPTY"]
        return todo_dict

DAO = TodoDAO()
#DAO.create({'task': 'Build an API'})
#DAO.create({'task': '?????'})
#DAO.create({'task': 'profit!'})


@ns.route('/')
class TodoList(Resource):
    '''Shows a list of all todos, and lets you POST to add new tasks'''
    @ns.doc('list_todos',security='AccessKey')
    @token_required_read
    @ns.marshal_list_with(todo)
    def get(self):
        '''List all tasks'''
        return DAO.getAll()

    @ns.doc('create_todo',security='AccessKey')
    @token_required_write
    @ns.expect(todo)
    @ns.marshal_with(todo, code=201)
    def post(self):
        '''Create a new task'''
        return DAO.create(api.payload), 201


@ns.route('/<int:id>')
@ns.response(404, 'Todo not found')
@ns.param('id', 'The task identifier')
class Todo(Resource):
    '''Show a single todo item and lets you delete them'''
    @ns.doc('get_todo',security='AccessKey')
    @token_required_read
    @ns.marshal_with(todo)
    def get(self, id):
        '''Fetch a given resource'''
        return DAO.get(id)

    @ns.doc('delete_todo',security="AccessKey")
    @token_required_write
    @ns.response(204, 'Todo deleted')
    def delete(self, id):
        '''Delete a task given its identifier'''
        DAO.delete(id)
        return '', 204

    @ns.doc('Update_todo',security="AccessKey")
    @token_required_write
    @ns.expect(todo_task)
    @ns.marshal_with(todo)
    def put(self, id):
        '''Update a task given its identifier'''
        return DAO.update(id, api.payload)



@ns.route('/status/<int:id>')
@ns.response(404,'Todo Not Found')    
@ns.param('id','The task identifier')
class TodoStatus(Resource):
    '''to change the status of the resource'''
    @ns.doc('Status_Updation',security="AccessKey")
    @token_required_write
    @ns.expect(todo_status)
    @ns.marshal_with(todo_status)
    def put(self,id):
        '''using PUT to change the status of the resource'''
        return DAO.updateStatus(id,api.payload)

@ns.route('/due')
@ns.response(404,'Todo Not Found')
class TodoDueDate(Resource):
    '''to check due tasks'''
    @ns.doc('View_Due_Tasks',security="AccessKey")
    @token_required_read
    def get(self):
        '''enter Due date in YYYY-MM-DD format to get current due tasks'''
        due_date=request.args.get("due_date")
        return DAO.tasksTobeFinished(due_date)

@ns.route('/overdue')
@ns.response(404,'Todo Task not found')
class todoOverDue(Resource):
    '''to get overdue tasks'''
    @ns.doc('Get_OverDue_Tasks',security="AccessKey")
    @token_required_read
    def get(self):
        '''to get the overdue tasks in the todoList'''
        return DAO.overdueTasks()

@ns.route('/finished')
@ns.response(404,'Todo Task not found')
class todoFinished(Resource):
    '''to get the finished tasks'''
    @ns.doc('Get_Finished_Tasks',security="AccessKey")
    @token_required_read
    def get(self):
        '''GET request to get all finished tasks'''
        return DAO.finished()

if __name__ == '__main__':
    app.run(debug=True)
