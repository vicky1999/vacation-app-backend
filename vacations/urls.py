from django.urls import path
from . import views

urlpatterns = [
    path('save/', views.Vacation.as_view()),
    path('get/<str:pk>/', views.Vacation.as_view()),
    path('list/', views.VacationsList.as_view()),
    path('update-status/', views.UpdateStatus.as_view()),
    path('delete/<int:id>', views.DeleteVacation.as_view())
]