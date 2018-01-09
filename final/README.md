# Linux Django course final

## python base

* Simple python program
if you set the envirment in your own computer
```
export PATH=$PATH:python_dir/bin
```
Then you can use the shell with the  shortcut key **ctrl + alt + T**</br>
and use the python shell you can do something</br>
like 1 + 1 then the shell will return 2 </br>
like len('string') then the shell will return 6 </br>
**We can use this way to do some base operate**

* Simple python grammer
the python base type is int double and char and we see the str dict list tuple as the complex type </br>
**In python:**

Define a variable  
```python
variable_string = ""
variable_list = []
variable_tuple = ()
variable_dict = {}
variable_int = 1
variable_float = 1.1
variable_char = 'A'
```
And use the base operator : </br>
**+ - * / % & ^ | and not**
you must be fammilar to this in C programming </br>

and the base structure operate : </br>
**FOR LOOP**
```python
for i in range(0,10):
  print(i)
```
It must same like this in C
```c
for(int i =0;i < 10;i++){
  printf("%d",i);
}
```
**WHILE LOOP**
```python
while True :
  print("True")

```
**IF ELSE**
```python
varl  = True
if varl :
  print("True")
else :
  print("False")  
```
Also in C
```c++
bool a = true;
if(a){
  cout << "True" << endl;
}else{
  cout << "False" << endl;
}
```

* Define function in python
we use the keyword **def** to define a function for example :
```python
def funct_name():
  print("Hello word")
```
And define a recursive function in python (Fibonacci Array ):
```python
def recursive_func(n):
  if n == 0 :
    return 1
  if n == 1 :
    return 1
  return recursive_func(n - 1)
```
But lambda is so difficult so for your interest find it by yourself </br>


* Object-oriented in python
Python let the object as the Ancestor class for any class in python and then we define all the class had inherited the object class </br>
**It is real same as Java**
we use the class to start define a class in python :
```python
class classA():
  #Class Body
```
and we let this class parents in the brackets:
```python
class classB(parent1,parent2):
  #Class body function and attributes
```
and we use the prefix **_** function name to define a private function in one class :
```python
class classC(object):
  def _func(self):
    print("I m private function")
```
and we can define a class we call person student  teacher:</br>
The inherite relationship like fllow :</br>
Person
----Student
----Teacher
```python

class Person(object):
  def __init__(self,name,age):
    self.name = name
    self.age = age
  def say_hello(self):
    print("Hello my name is %s",%self.name)

class Student(Person):
  def __init__(self,name,age,school):
    super(name,age)
    self.school = school
  def set_teacher(self,teacher):
    self.teacher = teacher
  def goto_school(self):
    print("I m %s I will goto %s",%(self.name,self.school))

class Teacher(Person):
  def __init__(self,name,age,school):
    super(name,age)
    self.school = school
  def say(self):
    print("hello i m teacher from %s",%self.school)

```

## Container base
We use the list dict and the tupe to make some complex structure in python we call this in java Container
and in python we say this is the base complex object </br>
and use this fllow three enough </br>
if use more conntainer we can  **import collection** </br>

* list
define a empty list is so easy just
```python
  list_name = []
```
find a element by index then use this way :
```python
list_name = []
list_name[index]
```
and this object have more native function :
```python
  list_name = []
  #append a element
  list_name.append(elemaent)
  #count a element
  list_name.count(element)
  #get the index of a element
  list_name.index(element)
  #remove a elemennt
  list_name.remove(element)
  #sort the elements
  list_name.sort(lambda x,y : x > y)
```
* tuple
The tuple like the list and the difference between their is that tuple is more like a set
In this container the elements is unique in this containe </br>
like this operatation:
```python
  tuple_name = ()
  #return the max in tuple
  max(tuple_name)
  # use the set() to be a tuple
  set(list)
```
* dict
When we use JSON we see the dict is like this structure</br>
simple define a dict :
```python
  dict_name = {}
```
Delete the dict
```python
  dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'};
  del dict['Name'];
  dict.clear();     
  del dict ;        
  print "dict['Age']: ", dict['Age'];
  print "dict['School']: ", dict['School'];
```
Modify the dict
```python
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'};
dict['Age'] = 8;
dict['School'] = "DPS School";
print "dict['Age']: ", dict['Age'];
print "dict['School']: ", dict['School'];
```

## Django base
Django is a framework for python web and we can use this to be a cms framework
and this framework is carry the admin system by itself </br>
My first personal blog is use this framework to contribute and is so easy for us to use

* What is the MTV pattern ?
  we call the **model** to be the data interface and surface </br>
  we call the **Template** to be the page display way </br>
  we call the **View** to be the router for user to find the correct Template and the model </br>
  </br>
  We can see the web service to a transcation contain a Request and a Response in some ways or such as that </br>
  Nginx and Apache will wrapper these to be two object and then will send them to the web container and we can find more information about the link from
  the two objects </br>
  and the Session is contain from many WebSession that containe just request and response so we must have a value to control the status of the user
  MTV is a way to let our code to be separated and we can maintain these easilier
  The view layer is on the base for the thing to control the view how to display and it seem as a base controller in the MVC pattern

* What is the Router ?
  we use the Router for us to let the user find the correct way for some business
  and then we use the url to do the same thing as the TCP/IP
  The common process is that when a request is comming then will let the Django to find the right url to handle this url</br>
  and then will use the bind handler to handle it and will let the handler to return the result to the endpoint user side

* How to start a Django ?
It is easy to solve this
    * Firstly you must install the Django on your conputer
    * Then use the pip to install the Django
    * How to do before two points ?
      like Ubuntu we should do this
        ```shell
          sudo apt-get install python
          sudo apt-get install pip
          pip install Django
          ```
And then choose the folder what is you favorite and then input this command that
**django-admin startproject your_project_name**</br>
and then change directory to the project folder
and then use this shell Command **python manage.py runserver** then your django is install successful
</br>
Django use the App to divide the business logic so we have to create our own app to create our business logic
use the command **python manage.py startapp app_name**</br>
and in your project directory will have a app directory and you can create your own logic of your app

* File Structure
  Base simple project structure
  ```
  mysite/
    manage.py
    mysite/
        __init__.py
        settings.py
        urls.py
        wsgi.py
  ```
  and containe one app or more apps
  ```
mysite/
  polls/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    views.py
  ```

* Create View one step
edit the **pools/views.py** and then write this
```python
from django.http import HttpResponse
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
```
Now you have create a simple view

* Modify the Url to map the view you have wrote
edit the **polls/urls.py**
```python
from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index, name='index'),
]
```
and edit the **mysite/urls.py**
```python
from django.conf.urls import include, url
from django.contrib import admin
urlpatterns = [
    url(r'^polls/', include('polls.urls')),
    url(r'^admin/', admin.site.urls),
]
```
you have mapped the base view on your url localhost:8000 /polls/ </br>

* Start use app and admin
Will open your project_name/project_name settings.py
and will set as below
```python
INSTALLED_APPS = (
  'django.contrib.admin',
  'django.contrib.auth',
  'django.contrib.contenttypes',
  'django.contrib.sessions',
  'django.contrib.messages',
  'django.contrib.staticfiles',
  'books',
)
```
and will register in admin to let the Django auto admin to admin this app
so modify this file **app_name/admin.py**
And write like this
```python
from django.contrib import admin
from myproject.myapp.models import Author

class AuthorAdmin(admin.ModelAdmin):
    pass
admin.site.register(Author, AuthorAdmin)
```

## Django more

* Model
  Use the model to define an object in the project so we can use the ORM to operate them
  Django model defined by inheriting the **djago.db.models.Model**
  ```python
  from django.db import models

  class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
  ```
  We use the models static function to create the fields for the truth model and the scrop object
  ```python
  models.CharField for character fields
  models.DataTimeField for datatimes
  models.IntegerField for integer
  models.TextField for a large text field
  models.BooleanField for a true or false field
  ```
  From the source code of Django I find that Django use the Template pattern to define this model way
  and then will use the same function to access the Database



## Question

* Program problem
    * How can you sort the Array  ?
        use the list.sort() function then will let a judge function in the sort inner
    * Get the definne key value in directory  
        ```python
          dict["key"]
        ```
    * Modify the dict ?
          ```python
            dict["key"] = "New Value"
          ```
    * Try to define a function to solve some algorithm problem
        * Bobble Sort ?
          ```python
            for i in range(0,n):
              for j in range(i,n):
                if list[i] < list[j]:
                    swap()    
          ```
        * Find the second Max elemennt
          ```python

          ```
        * Find the element that search in the search


* Django problem
  * Define a model simple
    you have to define a model to describe the person with name age and School
    ```python
      from django.db import models

      class Person(models.Model):
        name = models.CharField(max_length=20,null=False)
        age = models.IntegerField()
        school = models.CharField(max_length=30)
    ```
  * Define some models to describe the student-course releatioship
  ```python
  from django.db import models
  class Student(models.Model):
    name = models.CharField(max_length=30,null=False)
    age = models.IntegerField()
    course = models.ManyToMany('Course')
  class Course(models.Model)
    name = models.CharField(max_length=30)
    time = models.DateField()

  ```
  * Model query set
    * find the all record

    * conditional select

    * link select

    * many table select

    * ORM base
  
