from django.urls import path

from . import views

urlpatterns = [
    path('',views.classrooms, name='classrooms'),
    path('manage/',views.manage_classrooms, name='manage_classrooms'),
    path('streams/manage/',views.manage_streams, name='manage_streams'),
]
