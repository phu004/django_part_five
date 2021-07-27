from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Item, ToDoList, Person
from .forms import CreateNewList, CreatePerson

# Create your views here.
def index(request, name):
    ls = ToDoList.objects.get(name=name)
    return render(request, "main/list.html", {"ls": ls})

def home(request):
    ls = ToDoList.objects.all()
    return render(request, "main/home.html", {"list": ls})

def createList(request):
    if request.method == "POST":
        form = CreateNewList(request.POST)
        if form.is_valid():
            t = ToDoList(name=form.cleaned_data["name"])
            t.save()
        return HttpResponseRedirect("createList")
    else:
        form = CreateNewList()

    already_created = ToDoList.objects.all()
    data = {
            "form": form, 
            "create_title": "Create ToDoList", 
            "already_created": already_created
           }
    return render(request, "main/create.html", data)

def createPerson(request):
    if request.method == "POST":
        form = CreatePerson(request.POST)
        if form.is_valid():
            formData = form.cleaned_data
            p = Person(name=formData["name"], age=formData["age"], title=formData["title"])
            p.save()
        return HttpResponseRedirect("createPerson")
    else:
        form = CreatePerson()

    already_created = Person.objects.all()
    data = {
        "form": form, 
        "create_title": "Create Person", 
        "already_created": already_created
    }
    return render(request, "main/create.html", data)