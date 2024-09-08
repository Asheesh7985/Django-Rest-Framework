from django.urls import path
from restApplication import views

urlpatterns = [
   path('all-student/', views.AllStudentView,name='all-student'),
   path('single-student/<int:pk>/', views.SingleStudentView),
]