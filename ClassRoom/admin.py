from django.contrib import admin
from . models import Stream,Room,Teacher,Parent
# Register your models here.

admin.site.register(Stream)
admin.site.register(Room)

admin.site.register(Teacher)
admin.site.register(Parent)