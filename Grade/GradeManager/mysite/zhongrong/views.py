from django.shortcuts import render
from django.shortcuts import redirect
from django.template import RequestContext
from django.http import HttpResponse
from .models import Grade
# Create your views here.
def index(request):
    infos = Grade.objects.all()
    return render(request, 'index.html', {'infos': infos})

def add(request):
    if request.method == 'POST' :
        classname=request.POST.get('classname')
        number=request.POST.get('number')
        info=Grade(classname=classname,number=number)
        info.save()
        return redirect('/')
    return render(request,'add.html')

def delete(request):
    name=request.GET.get('classname')
    Grade.objects.filter(classname=name).delete()

    return redirect('/')

def change(request):
    classname=request.GET.get('classname')
    Grade.objects.filter(classname=classname).delete()
    return render(request,'add.html')


    
