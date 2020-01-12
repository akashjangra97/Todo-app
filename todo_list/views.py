from django.shortcuts import render,redirect
from .models import List
from .forms import ListForm
from django.contrib import messages

# Create your views here.
def home(request):
    if request.method == 'POST': # if somebody fills out the form then its a post request and then save the form if form is valid
        form = ListForm(request.POST)
        if form.is_valid():
            form.save()
            all_items = List.objects.all() # then we can push the items in database and 
            messages.success(request,"Item has been added")
            return render(request,'home.html',{'all_items':all_items}) # then return to home page  and access all the items that has been added by using a dictionary 
            # if this return is not present then it will save the data but doesnt able to return to the home page

    else:
        all_items = List.objects.all() # otherwise show the page with the items 
        return render(request,'home.html',{'all_items':all_items})

def delete(request,list_id):
    item = List.objects.get(pk=list_id)
    item.delete()
    messages.success(request,"Item has been deleted")
    return redirect('home')

def cross_off(request,list_id):
    Item = List.objects.get(pk=list_id)
    Item.completed = True
    Item.save()
    return redirect('home')

def uncross(request,list_id):
    Item = List.objects.get(pk=list_id)
    Item.completed = False
    Item.save()
    return redirect('home')


def edit(request,list_id):
    if request.method == 'POST': 
        Item = List.objects.get(pk=list_id)
        form = ListForm(request.POST or None,instance=Item)
        if form.is_valid():
            form.save()
             
            messages.success(request,"Item has been Edited")
            return redirect('home') 

    else:
        Item = List.objects.get(pk=list_id)  
        return render(request,'edit.html',{'Item':Item})


