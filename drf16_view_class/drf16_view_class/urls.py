"""
URL configuration for drf16_view_class project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from restApplication import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create-employee/', views.EmployeeCreateView.as_view()),
    path('all-employee/',views.AllEmployeeView.as_view()),
    path('single-employee/<int:pk>/', views.SingleEmployeeView.as_view()),
    path('update-employee/<int:pk>/', views.UpdateEmployeeView.as_view()),
    path('delete-employee/<int:pk>/',views.DeleteEmployee.as_view()),
]
