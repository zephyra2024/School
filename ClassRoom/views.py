from django.shortcuts import render,redirect

from django.urls import reverse

from django.http import HttpResponse

from .models import Room,Stream

from .forms import RoomForm,StreamForm,editRoomForm,editStreamForm

# Create your views here.

def classrooms(request):
    
    context ={
        'total_rooms' : Room.objects.all().count(),
        'total_streams' : Stream.objects.all().count(),  
    }
    return render(request,'ClassRoom/rooms.html',context)

def view_classrooms(request):
    context = {
        'rooms' : Room.objects.all(),

    }
    return render(request,'ClassRoom/view.html',context)

def edit_classroom(request,id):
    room = Room.objects.get(pk=id)
    print(room.room_id)
    if request.method == 'POST':
        form = editRoomForm(request.POST,instance=room)
        if form.is_valid():
            form.save()
            print('saved')
            return redirect(reverse('manage_classrooms') + '?edited=true')
        print('invalid')
        return render(request,'ClassRoom/edit.html',context={'room_form':form,'room':room})
    else:
        form = editRoomForm(instance=room)
    return render(request,'ClassRoom/edit.html',context={'room_form':form,'room':room})


def edit_stream(request,id):
    stream = Stream.objects.get(pk=id)
    
    if request.method == 'POST':
        form = editStreamForm(request.POST,instance=stream)
        if form.is_valid():
            form.save()
            print('saved')
            return redirect(reverse('manage_streams') + '?edited=true')
        print('Invalid form for edditing stream')
        
        return render(request,'ClassRoom/edit.html',context={'room_form':form,'stream':stream})
    else:
        form = editStreamForm(instance=stream)
    return render(request,'ClassRoom/edit.html',context={'room_form':form,'stream':stream})

def view_streams(request):
    context = {
        'streams' : Stream.objects.all(),
    }
    return render(request,'ClassRoom/view.html',context)

def add_stream(request):
    form = StreamForm()
    if request.method == 'POST':
        form = StreamForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('manage_streams')+'?added=true')
        return render(request,'ClassRoom/add.html',{'addstreamForm':form})
    return render(request,'ClassRoom/add.html',{'addstreamForm':form})

def add_room(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('manage_streams')+'?added=true')
        return render(request,'ClassRoom/add.html',{'addroomForm':form})
    return render(request,'ClassRoom/add.html',{'addroomForm':form})