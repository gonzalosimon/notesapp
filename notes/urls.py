# In notes/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create_note, name='create_note'),
    path('note/<int:pk>/', views.note_detail, name='note_detail'),
    path('delete/<int:pk>/', views.delete_note, name='note_delete'),
    path('edit/<int:pk>/', views.edit_note, name='edit_note'),
    path('about/', views.about, name='about'),
]
