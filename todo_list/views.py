from django.shortcuts import render,redirect
from .models import List
from .forms import ListForms
from django.contrib import messages
from django.http import HttpResponseRedirect

# Create your views here.
def home(request):
    if request.method == "POST":
        form=ListForms(request.POST or NONE)
        if form.is_valid():
            form.save()
            all_items=List.objects.all
            messages.success(request,("Items are added to the List"))
            return render(request,'home.html',{'all_items':all_items})
    else:
        all_items=List.objects.all
        return render(request,'home.html',{'all_items':all_items})

def about(request):
    return render(request,'about.html',{})    

def delete(request,list_id):
    item=List.objects.get(pk=list_id)
    item.delete() 
    messages.success(request,("Item has been deleted from the List"))
    return redirect('home')

def cross_off(request,list_id):
    item=List.objects.get(pk=list_id)
    item.completed=True
    item.save()
    return redirect('home')

def uncross(request,list_id):
    item=List.objects.get(pk=list_id)
    item.completed=False
    item.save()
    return redirect('home')    


def edit(request,list_id):
    if request.method == "POST":
        item=List.objects.get(pk=list_id)
        form=ListForms(request.POST or NONE,instance=item)
        if form.is_valid():
            form.save()
            
            messages.success(request,("Items has been Edited!"))
            return redirect('home')
    else:
        item=List.objects.get(pk=list_id)
        return render(request,'edit.html',{'item':item})

