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
Add a new path in "urls.py" so the user could reach this form by typing the path "/main/createPerson". The path should use a view function called "createPerson" in views.py. 
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
    
Add the view function "createPerson" in views.py. We are going to reuse the template file "create.html" to render the page. For the third parmemter in the render method use an empty dictionary for the time being.
<details>
  <summary>Click for solution</summary>
      
```sh
def createPerson(response):
    data = {
    }
    return render(response, "main/create.html", data)
```
</details>
    
 <br/><br/>
    
## 3. Create a Django from for the "Person" model
In forms.py, add a new class called "CreatePerson" that inherits the Django form. Then for each attribute in the "Person" model, create the corrisponding attributes for the "CreatePerson" class.
    <details>
  <summary>Click for solution</summary>
      
```sh
class CreatePerson(forms.Form):
    name = forms.CharField(max_length=200)
    age = forms.IntegerField()
    title = forms.CharField(max_length=200)
```
</details>
    
Now go back to views.py, first modify the "import" line so Django knows about the new form class we just created.
    <details>
  <summary>Click for solution</summary>
      
```sh
from .forms import CreateNewList, CreatePerson
```
</details>
Then expand the dictionary data with 3 key pairs:
- "form" should map to a new "CreatePerson" object
- "create_title" should map to the string "Create Person"
- "already_created" should map to a list of objects that have been created for the "Person" model
    
```sh
class CreatePerson(forms.Form):
    name = forms.CharField(max_length=200)
    age = forms.IntegerField()
    title = forms.CharField(max_length=200)
```
</details>
