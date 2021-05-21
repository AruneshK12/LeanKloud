from flask import Flask
from flask_restplus import Api, Resource, fields
from werkzeug.middleware.proxy_fix import ProxyFix
import mysql.connector

mydb=mysql.connector.connect(host="localhost",username="root",password="ADMIN",database="test")

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)
api = Api(app, version='1.0', title='TodoMVC API',
    description='A simple TodoMVC API',
)

ns = api.namespace('todos', description='TODO operations')

todo = api.model('Todo', {
    'id': fields.Integer(readonly=True, description='The task unique identifier'),
    'task': fields.String(required=True, description='The task details'),
    'due by': fields.String(required=True, description='The due date of task in YYYY-MM-DD format'),
    'Status': fields.String(required=True, description="Current status of task")
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
        query="UPDATE todoList set Status=%s where id="+str(id)
        val=(stat,)
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
        todo={}
        todo['task']=task
        todo['id']=id
        return todo

    def delete(self, id):
        myc1=mydb.cursor()
        query="DELETE FROM todoList where id="+str(id)
        myc1.execute(query)
        mydb.commit()


DAO = TodoDAO()
#DAO.create({'task': 'Build an API'})
#DAO.create({'task': '?????'})
#DAO.create({'task': 'profit!'})


@ns.route('/')
class TodoList(Resource):
    '''Shows a list of all todos, and lets you POST to add new tasks'''
    @ns.doc('list_todos')
    @ns.marshal_list_with(todo)
    def get(self):
        '''List all tasks'''
        return DAO.getAll()

    @ns.doc('create_todo')
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
    @ns.doc('get_todo')
    @ns.marshal_with(todo)
    def get(self, id):
        '''Fetch a given resource'''
        return DAO.get(id)

    @ns.doc('delete_todo')
    @ns.response(204, 'Todo deleted')
    def delete(self, id):
        '''Delete a task given its identifier'''
        DAO.delete(id)
        return '', 204

    @ns.expect(todo)
    @ns.marshal_with(todo)
    def put(self, id):
        '''Update a task given its identifier'''
        return DAO.update(id, api.payload)

    

if __name__ == '__main__':
    app.run(debug=True)
