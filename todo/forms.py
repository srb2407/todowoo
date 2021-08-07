from django.forms import ModelForm
from django.forms import fields
from .models import ToDo


class ToDoForm(ModelForm):
    class Meta:
        model = ToDo
        fields = ['title', 'memo', 'important']
