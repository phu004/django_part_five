# Django Workshop Exercise 5

In this exercise we will learn how to use the Django "form" to create HTML forms and submit the result into the database. 
<br/><br/>
## 1. Prepare for the coding environment  

SSH into the test machine. The password is 123456.
```sh
ssh your_upi@130.216.39.213
```
Once you are in, activate the python virtual environment and cd into the project folder
```sh
workon dj && cd mysite
```
<br/><br/>

## 2. Setting up routing and view function for the form page.
A new model "Person" was addedd into the "main" app, you can find its defintion in "models.py" Our Goal is to create a form page which allows you to add "Person" objects into the database.
```sh
class Person(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.name
```
Add a new path in "urls.py" so the user could reach this form by typing the path "/main/createList". The path should use a view function called "createList" in views.py. 
<details>
  <summary>Click for solution</summary>
  
```sh
urlpatterns = [
        path('createList', views.createList),
        path('<str:name>', views.index),
        path('', views.home),   
]
```
</details>
