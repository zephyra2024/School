from django.db import models
from django.core.exceptions import ValidationError

from django.db.models.signals import post_save,pre_save,post_delete
from django.dispatch import receiver



from . import signals

class Teacher(models.Model):
    name = models.CharField(max_length=22,primary_key=True)
class Parent(models.Model):
    name = models.CharField(max_length=22,primary_key=True)
    
class Student(models.Model):
    name = models.CharField(max_length=22,primary_key=True)
    
    
class Room(models.Model):
    room_id = models.CharField(max_length=55, primary_key=True, null=False, blank=False,verbose_name='Class ID')
    room_name = models.CharField(max_length=255, null=False, blank=False, unique=True,verbose_name='Class Name')
    room_teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE,null=True,blank=True,verbose_name='Class Teacher')
    room_representative = models.ForeignKey(Parent, on_delete=models.CASCADE,null=True,blank=True,verbose_name='Class Representative')
    room_count = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.room_name
    
    def clean(self):
        super().clean()
        
        if self.room_teacher:  # Check if stream_teacher is not None

            # Check if stream_teacher exists in Teacher database
            
            if not Teacher.objects.filter(pk=self.room_teacher.pk).exists():
                raise ValidationError({'stream_teacher': 'Teacher does not exist.'})

        if self.room_representative:  # Check if stream_representative is not None
            try:
                # Check if stream_representative exists in Parent database
                if not Parent.objects.filter(pk=self.room_representative.pk).exists():
                    raise ValidationError({'stream_representative': 'Parent does not exist.'})
            except Parent.DoesNotExist:
                raise ValidationError({'stream_representative': 'Parent does not exist.'})

            
    def save(self, *args, **kwargs):
        self.full_clean()  # Validate the model before saving
        super().save(*args, **kwargs)
    

class Stream(models.Model):
    stream_id = models.CharField(max_length=55, primary_key=True, null=False, blank=False)
    stream_name = models.CharField(max_length=255, null=False, blank=False, unique=True)
    stream_room = models.ForeignKey(Room,on_delete=models.CASCADE)
    stream_teacher = models.OneToOneField(Teacher, on_delete=models.CASCADE, null=True,blank=True)
    stream_representative = models.OneToOneField(Parent, on_delete=models.CASCADE, null=True,blank=True)
    stream_prefect = models.ForeignKey(Student,max_length=255, null=True,blank=True,on_delete=models.CASCADE)
    stream_count = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return f'{self.stream_room} - {self.stream_name}'

    def clean(self):
        super().clean()
        
        if self.stream_teacher:  # Check if stream_teacher is not None

            # Check if stream_teacher exists in Teacher database
            
            if not Teacher.objects.filter(pk=self.stream_teacher.pk).exists():
                raise ValidationError({'stream_teacher': 'Teacher does not exist.'})

        if self.stream_representative:  # Check if stream_representative is not None
            try:
                # Check if stream_representative exists in Parent database
                if not Parent.objects.filter(pk=self.stream_representative.pk).exists():
                    raise ValidationError({'stream_representative': 'Parent does not exist.'})
            except Parent.DoesNotExist:
                raise ValidationError({'stream_representative': 'Parent does not exist.'})

            
    def save(self, *args, **kwargs):
        self.full_clean()  # Validate the model before saving
        super().save(*args, **kwargs)
        





post_save.connect(signals.increment_room_count,sender=Stream)   
post_delete.connect(signals.decrement_room_count,sender=Stream)     