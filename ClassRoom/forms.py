
from django import forms

from .models import Room,Stream

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields =['room_id','room_name','room_teacher','room_representative',]
        widgets = {
            'room_id':forms.TextInput(attrs={'class':'form-control'}),
            'room_name':forms.TextInput(attrs={'class':'form-control'}),
            'room_teacher':forms.Select(attrs={'class':'form-control'}),
            'room_representative':forms.Select(attrs={'class':'form-control'}),
        }

class editRoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields =['room_id','room_name','room_teacher','room_representative',]
        widgets = {
            'room_id':forms.TextInput(attrs={'class':'form-control','readonly':True}),
            'room_name':forms.TextInput(attrs={'class':'form-control','readonly':True}),
            'room_teacher':forms.Select(attrs={'class':'form-control'}),
            'room_representative':forms.Select(attrs={'class':'form-control'}),
        }       
        
class StreamForm(forms.ModelForm):
    class Meta:
        model = Stream
        fields =['stream_id','stream_name','stream_room','stream_teacher','stream_representative','stream_prefect']
        widgets ={
            'stream_id':forms.TextInput(attrs={'class':'form-control',}),
            'stream_name':forms.TextInput(attrs={'class':'form-control'}),
            'stream_room':forms.Select(attrs={'class':'form-control'}),
            'stream_teacher':forms.Select(attrs={'class':'form-control'}),
            'stream_representative':forms.Select(attrs={'class':'form-control'}),
            'stream_prefect':forms.TextInput(attrs={'class':'form-control'}),
            
        }
        
class editStreamForm(forms.ModelForm):
    class Meta:
        model = Stream
        fields =['stream_id','stream_name','stream_room','stream_teacher','stream_representative','stream_prefect']
        widgets ={
            'stream_id':forms.TextInput(attrs={'class':'form-control','readonly':True}),
            'stream_name':forms.TextInput(attrs={'class':'form-control'}),
            'stream_room':forms.Select(attrs={'class':'form-control','readonly':True}),
            'stream_teacher':forms.Select(attrs={'class':'form-control'}),
            'stream_representative':forms.Select(attrs={'class':'form-control'}),
            'stream_prefect':forms.TextInput(attrs={'class':'form-control'}),
            
        }