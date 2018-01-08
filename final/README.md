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
  list_name.sort(lambda x,y : x > y ? : True : False)
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
When we use JSON we see the dict is like this structure

## Django base

## Question
