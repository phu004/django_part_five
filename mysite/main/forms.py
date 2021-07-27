from django import forms

class CreateNewList(forms.Form):
    name = forms.CharField(max_length=200)
    check = forms.BooleanField(required=False)

class CreatePerson(forms.Form):
    name = forms.CharField(max_length=200)
    age = forms.IntegerField()
    title = forms.CharField(max_length=200)