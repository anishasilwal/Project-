from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('upload/', views.upload_file, name='upload_file'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]
