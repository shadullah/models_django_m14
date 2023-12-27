from django.shortcuts import render, redirect
from . import models
# Create your views here.
def home(req):
    student = models.Student.objects.all()
    # print(student)
    return render(req, 'models_app/home.html', {'data': student})

def deleteStu(req, roll):
    std = models.Student.objects.get(pk=roll).delete()
    return redirect('homepage')
