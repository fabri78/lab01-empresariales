from django.urls import path
from . import views

urlpatterns = [
    path('app/sumar/<int:num1>/<int:num2>/', views.sumar, name='sumar'),
]