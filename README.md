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
  ## Part - 1 output recording link: [Click here](https://drive.google.com/file/d/1FbDT-HLsim9MzajOZqm__K8zpMwLctSk/view?usp=sharing)
  ## Part - 1 Screenshots: -   \[Using Curl Operations\]
  
  The Database Screenshot is as follows: -  
  ![image](https://user-images.githubusercontent.com/34567890/119234497-d5de7780-bb4b-11eb-8454-a3c383dc09bd.png)

  
  1. To get all the tasks:  
  ![image](https://user-images.githubusercontent.com/34567890/119234123-d7a73b80-bb49-11eb-9bd3-d9661e2bb4bf.png)

  2. To Add a new Task:  
  ![image](https://user-images.githubusercontent.com/34567890/119234194-3bc9ff80-bb4a-11eb-8648-074e1ba34c4c.png)

  3. To get a specific task:  
  ![image](https://user-images.githubusercontent.com/34567890/119234211-5308ed00-bb4a-11eb-8c70-70c15bed7a4c.png)

  4. To update a task name:  
  ![image](https://user-images.githubusercontent.com/34567890/119234231-6c119e00-bb4a-11eb-9e29-398b20c17cd3.png)
  
  5. To delete a task:  
  ![image](https://user-images.githubusercontent.com/34567890/119234315-f0fcb780-bb4a-11eb-99bc-a16543496da9.png)

  6. To update the status of a task:  
  ![image](https://user-images.githubusercontent.com/34567890/119234332-0540b480-bb4b-11eb-9ffc-da88205310ad.png)

  7. To see finished tasks:  
  ![image](https://user-images.githubusercontent.com/34567890/119234343-125da380-bb4b-11eb-9ed8-bc6649f0da2d.png)

  8. To see tasks due on 21-05-2021:  
  ![image](https://user-images.githubusercontent.com/34567890/119234383-3e792480-bb4b-11eb-89df-946cf40290a2.png)

  9. To see overdue tasks as of 23-05-2021:  
  ![image](https://user-images.githubusercontent.com/34567890/119234393-4fc23100-bb4b-11eb-9864-788d9f047df9.png)

  10. Example of only Read access: \[token usertemp has only Read access hence no delete operations can be performed\]  
  ![image](https://user-images.githubusercontent.com/34567890/119234403-610b3d80-bb4b-11eb-8cca-799ddb9ad18a.png)

  11. Example of only Write Access: \[token WriteAccess has only write access hence no viewing tasks operations can be performed\]  
  ![image](https://user-images.githubusercontent.com/34567890/119234434-84ce8380-bb4b-11eb-88aa-e100be613131.png)

  12. Example of Unknown token access: \[token qwerty doesnt exist in the database accessKeys\]  
  ![image](https://user-images.githubusercontent.com/34567890/119234480-b9dad600-bb4b-11eb-91e2-c068706ff7f1.png)

  
## Part - 2
  ### The complexity of the topper_calc.py is O(n). 
  The reason is there are 2 loops that are ran for the total n records and the topper of each subject and ranking marks are found in O(n) while the matching with names is done with another loop in O(n) time.  
  O(n) is Big O Notation and refers to the complexity of a given algorithm. n refers to the size of the input, in your case it's the number of items in your list. O(n) means that the algorithm will take on the order of n operations to find the toppers.
  
  The screenshots of the output is as follows: -  
  ![image](https://user-images.githubusercontent.com/34567890/119223322-61d5ac80-bb16-11eb-952e-f66870bcced4.png)
