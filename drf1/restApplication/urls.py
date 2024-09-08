from django.urls import path
from restApplication import views

urlpatterns = [
    path('student-detail/<int:pk>/', views.Student_detail,name='student=detail'),
    path('all-student/', views.AllStudent,name='all-student'),
]
