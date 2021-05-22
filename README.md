# LeanKloud
Python Programming Test - LeanKloud for Arunesh Kumar

## Part - 1
  In this Part - 1 we have created an Flask-RESTful API task List manager, the basic code used is found in [todoMVC](https://flask-restplus.readthedocs.io/en/stable/example.html). In this API the following functionalities are present:-  
> 1. Ability to add, view, delete and update tasks  
> 2. Ability to check the due tasks based on the given due date  
> 3. Ability to check the overdue tasks  
> 4. Ability to check the tasks which have been finished  
> 5. A token Based authenication with Read, Write and ReadWrite Access types

  A given Todo has the following Attributes: -  
  ```
  todo = api.model('Todo', {
    'id': fields.Integer(readonly=True, description='The task unique identifier'),
    'task': fields.String(required=True, description='The task details'),
    'due by': fields.String(required=True, description='The due date of task in YYYY-MM-DD format'),
    'Status': fields.String(required=True, description="Current status of task")
})
  ```  
  
  Please Make sure the following packages are present for Running Part-1 Flask-RESTful todoMVC: -  
```
MYSQL Command Client 8.0
mysql connector for Python
Python 3.7
flask
flask_restplus
Werkzeug
functools
```
  The tables being used in the given API are: -
  > 1. TodoList table: 
  > > This table has all the attributes required in the API
  > > The create table code is as follows: -
  > > >
  ```
  CREATE TABLE todoList(
   -> id int NOT NULL Auto_increment primary key,
   -> task varchar(30),
   -> DueBy date,
   -> Status varchar(20) DEFAULT 'Not Started',
   -> constraint todo_status_con CHECK ( status IN ('Not Started','In Progress','Finished'))
   -> );
  ```
  > 2. AcessKeys table:
  > > This table has the access keys and the access types for each key to access the given API
  > > There are 3 types of AccessTypes:-
  > > >  0 ==> Read Access : The user can only view the tasks and status  
  > > >  1 ==> Write Access : The user can only create and update the tasks and status  
  > > >  2 ==> Read And Write Access : Both functionalities of READ and WRITE access are present  
  ```
  CREATE TABLE AcessKeys(
  -> KeyName varchar(20),
  -> AcessType int
  -> );
  ```
  Change the following line in todo.py with the required details: -
  ```
  mydb=mysql.connector.connect(host="<Database Host Name>",username="<MYSQL Username>",password="<MYSQL Password>",database="<database where the tables are created>")
  ```

## Part - 2
  The complexity of the topper_calc.py is O(n).  
  The screenshots of the output is as follows: -  
  ![image](https://user-images.githubusercontent.com/34567890/119223322-61d5ac80-bb16-11eb-952e-f66870bcced4.png)
