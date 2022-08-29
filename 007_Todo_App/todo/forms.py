from dataclasses import fields
from socket import fromshare
from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields= "__all__"