from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import generic

from . models import TodoModel
from .forms import TodoForm

def listview(request):
    contents = TodoModel.objects.all()
    return render(request, 'index.html', {'all_items': contents})

def addItem(request):
    title = request.POST['title']
    description = request.POST['description']
    new_item = TodoModel()
    new_item.title = title
    new_item.description = description
    new_item.save()
    return HttpResponseRedirect('/todoapp/')

def deleteItem(request, i):
    y = TodoModel.objects.get(id=i)
    y.delete()
    return HttpResponseRedirect('/todoapp/')

# def editItem(request, i):

def editItem(request, i):
    obj = TodoModel.objects.get(id=i)
    mydictionary = {
        "title" : obj.title,
        "description" : obj.description,
    }
    return render(request,'edit.html',context=mydictionary)



# Create your views here.
