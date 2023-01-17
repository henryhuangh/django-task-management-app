from django import forms
from .models import ToDos

class CreateToDo(forms.ModelForm):
    class Meta:
        model = ToDos
        fields = '__all__'