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
        if self.room_teacher:  # Check if room_teacher is not None
            try:
                # Check if stream_teacher exists in Teacher database
                if not Teacher.objects.filter(pk=self.room_teacher).exists():
                    raise ValidationError({'stream_teacher': 'Teacher does not exist.'})
            except Teacher.DoesNotExist:
                raise ValidationError({'stream_teacher': 'Teacher does not exist.'})

        if self.room_representative:  # Check if room_representative is not None
            try:
                # Check if stream_representative exists in Parent database
                if not Parent.objects.filter(pk=self.room_representative).exists():
                    raise ValidationError({'stream_representative': 'Parent does not exist.'})
            except Parent.DoesNotExist:
                raise ValidationError({'stream_representative': 'Parent does not exist.'})

    def save(self, *args, **kwargs):
        self.full_clean()  # Validate the model before saving
        super().save(*args, **kwargs)


class Stream(models.Model):
    stream_id = models.CharField(max_length=55, primary_key=True, null=False, blank=False)
    stream_name = models.CharField(max_length=255, null=False, blank=False, unique=True)
    stream_teacher = models.ForeignKey('Teacher', on_delete=models.CASCADE, null=True)
    stream_representative = models.ForeignKey('Parent', on_delete=models.CASCADE, null=True)
    stream_prefect = models.CharField(max_length=255, null=True)
    stream_count = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.stream_name

    def clean(self):
        super().clean()
        if self.stream_teacher:  # Check if stream_teacher is not None
            try:
                # Check if stream_teacher exists in Teacher database
                if not Teacher.objects.filter(pk=self.stream_teacher).exists():
                    raise ValidationError({'stream_teacher': 'Teacher does not exist.'})
            except Teacher.DoesNotExist:
                raise ValidationError({'stream_teacher': 'Teacher does not exist.'})

        if self.stream_representative:  # Check if stream_representative is not None
            try:
                # Check if stream_representative exists in Parent database
                if not Parent.objects.filter(pk=self.stream_representative).exists():
                    raise ValidationError({'stream_representative': 'Parent does not exist.'})
            except Parent.DoesNotExist:
                raise ValidationError({'stream_representative': 'Parent does not exist.'})

    def save(self, *args, **kwargs):
        self.full_clean()  # Validate the model before saving
        super().save(*args, **kwargs)

class Teacher(models.Model):
    name = models.CharField(max_length=22)
class Parent(models.Model):
    name = models.CharField(max_length=22)