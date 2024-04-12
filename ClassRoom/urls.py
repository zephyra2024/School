from django.urls import path

from . import views

urlpatterns = [
    path('',views.classrooms, name='classrooms'),
    path('view/',views.view_classrooms, name='manage_classrooms'),
    path('streams/view/',views.view_streams, name='manage_streams'),
    
    path('streams/manage/edit/<str:id>',views.edit_stream,name='manage-stream'),
    path('manage/edit/<str:id>',views.edit_classroom,name='manage-room'),
    
    path('stream/add/',views.add_stream,name='add-stream'),
    path('room/add/',views.add_room,name='add-room'),
    
    
    
]
