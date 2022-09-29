from cProfile import label
from todolist.models import toDoList
from django.forms import ModelForm

class todoForm(ModelForm):
    class Meta:
        model = toDoList
        fields = ['title','description','finished',]