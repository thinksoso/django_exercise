from django.shortcuts import render
from django.shortcuts import redirect
from django.template import RequestContext
from django.http import HttpResponse
from .models import Book
# Create your views here.
def index(request):
    book_infos = Book.objects.all()
    return render(request, 'index.html', {'book_infos': book_infos})

def add(request):
    if request.method == 'POST' :
        name=request.POST.get('name')
        author=request.POST.get('author')
        amount=request.POST.get('amount')
        book_info=Book(name=name,author=author,amount=amount)
        book_info.save()
        return redirect('/')
    return render(request,'add.html')

def delete(request):
    name=request.GET.get('name')
    Book.objects.filter(name=name).delete()

    return redirect('/')

def change(request):
    name=request.GET.get('name')
    Book.objects.filter(name=name).delete()
    return render(request,'add.html')


    
