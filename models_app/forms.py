from django import forms 
from models_app.models import Student

class studentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'roll', ]