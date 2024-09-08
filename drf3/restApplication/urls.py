from django.urls import path
from restApplication import views

urlpatterns = [
    path('add-student/', views.Student_data,name='add-student'),
]
