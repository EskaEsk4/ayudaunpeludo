from django.contrib import admin
from django.urls import path
from webONG import views
urlpatterns = [
    path ('', views.index, name ='INDEX'),
    path('perros/', views.perros, name='PERROS'),
    path ('gatos/', views.gatos, name='GATOS'),
    path ('coraje/', views.coraje, name='CORAJE'),
    path ('doraemon/', views.doraemon, name='DORAEMON'),
    path ('garfield/', views.garfield, name='GARFIELD'),
    path ('patan/', views.patan, name='PATAN'),
    path ('scooby/', views.scooby, name='SCOOBY'),
    path ('tom/', views.tom, name='TOM'),

]