from django import forms
from App.models import *

class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields='__all__'
        