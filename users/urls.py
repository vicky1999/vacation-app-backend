from atexit import register
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.Login.as_view()),
    path('register/', views.Register.as_view()),
    path('list/', views.ListEmployees.as_view()),
    path('update/', views.UpdateEmployees.as_view()),
    path('delete/<int:id>', views.DeleteEmployee.as_view())
]