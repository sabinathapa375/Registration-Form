from . import views
from django.urls import path


urlpatterns = [
    path('register/', views.registerForm, name='register'),
    path('login/', views.loginFormm, name='login')
]
