from django.urls import path
from . import views
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('', views.index, name='index'),
    path('acerca/', views.about, name='about'),
    path('bienvenido/', views.welcome, name='welcome'),
    path('logout/', views.logout_view, name='logout'),
    path('contacto/', views.contact, name='contact'),
    path('exito/', views.success, name='success'),
    path('flan/<int:pk>/', views.flan_detail, name='flan_detail'),
    path('flan/<int:pk>/review/', views.add_review, name='add_review'),
    path('flanes/', views.flan_list, name='flan_list'),
]
