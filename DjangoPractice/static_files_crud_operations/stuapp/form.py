from operator import imod
from django import forms
from stuapp.models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"
        
