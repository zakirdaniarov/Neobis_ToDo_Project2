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
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/todoapp/')
    else:
        form = TodoForm(instance=obj)

    return render(request, 'edit.html', {'form': form})



# Create your views here.
