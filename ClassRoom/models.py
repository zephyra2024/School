from django.db import models
from django.core.exceptions import ValidationError

class Room(models.Model):
    room_id = models.CharField(max_length=55, primary_key=True, null=False, blank=False)
    room_name = models.CharField(max_length=255, null=False, blank=False, unique=True)
    room_teacher = models.ForeignKey('Teacher', on_delete=models.CASCADE)
    room_representative = models.ForeignKey('Parent', on_delete=models.CASCADE)
    room_count = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.room_name

    def clean(self):
        super().clean()
        try:
            # Check if room_teacher exists in Teacher database
            if not Teacher.objects.filter(pk=self.room_teacher_id).exists():
                raise ValidationError({'room_teacher': 'Teacher does not exist.'})
            
            # Check if room_representative exists in Parent database
            if not Parent.objects.filter(pk=self.room_representative_id).exists():
                raise ValidationError({'room_representative': 'Parent does not exist.'})
        except:
            pass

    def save(self, *args, **kwargs):
        self.full_clean()  # Validate the model before saving
        super().save(*args, **kwargs)

class Stream(models.Model):
    stream_id = models.CharField(max_length=55, primary_key=True, null=False, blank=False)
    stream_name = models.CharField(max_length=255, null=False, blank=False, unique=True)
    stream_teacher = models.ForeignKey('Teacher', on_delete=models.CASCADE)
    stream_representative = models.ForeignKey('Parent', on_delete=models.CASCADE)
    stream_prefect = models.CharField(max_length=255,null=True)
    stream_count = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.stream_name

    def clean(self):
        super().clean()
        try:
            # Check if room_teacher exists in Teacher database
            if not Teacher.objects.filter(pk=self.stream_teacher_id).exists():
                raise ValidationError({'stream_teacher': 'Teacher does not exist.'})
            
            # Check if room_representative exists in Parent database
            if not Parent.objects.filter(pk=self.stream_representative_id).exists():
                raise ValidationError({'stream_representative': 'Parent does not exist.'})
        except:
            pass
    def save(self, *args, **kwargs):
        self.full_clean()  # Validate the model before saving
        super().save(*args, **kwargs)
        
class Teacher(models.Model):
    name = models.CharField(max_length=22)
class Parent(models.Model):
    name = models.CharField(max_length=22)