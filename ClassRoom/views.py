from django.shortcuts import render

from django.http import HttpResponse

from .models import Room,Stream

# Create your views here.

def classrooms(request):
    
    context ={
        'total_rooms' : Room.objects.all().count(),
        'total_streams' : Stream.objects.all().count(),
        
        
    }
    return render(request,'ClassRoom/rooms.html',context)

def manage_classrooms(request):
    context = {
        'rooms' : Room.objects.all(),

    }
    return render(request,'ClassRoom/manage.html',context)

def manage_streams(request):
    context = {
        'streams' : Stream.objects.all(),
    }
    return render(request,'ClassRoom/manage.html',context)