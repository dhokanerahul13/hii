from django.forms import ModelForm
from django.shortcuts import render
from stu.forms import movieform
from stu.models import movie
# Create your views here.

def add_movie(request):
    form=movieform()
    if request.method=="POST":
        form=movieform(request.POST)
        if form.is_valid():
            form.save()
    return render(request,'stu/index.html',{'form':form})        