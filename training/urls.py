from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('sessions/', views.session_list, name='session_list'),
    path('sessions/new/', views.session_create, name='session_create'),
    path('sessions/<int:id>/edit/', views.session_edit, name='session_edit'),
    path('sessions/<int:id>/delete/', views.session_delete, name='session_delete'),
    path('register/', views.register, name='register'),
]