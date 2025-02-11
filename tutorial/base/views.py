from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
rooms = [
    {'id':1, 'name':'Lets learn python!'},
    {'id':2, 'name':'Lets foot foot ball !'},
    {'id':3, 'name':'fonender learn !'},
    

]
def home(request):
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)
def room(request,pk):
   return render(request, 'base/room.html')
