from django.contrib import admin
from django.urls import path,include
from restApp import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('employee-api', views.EmployeeAPIView,basename='Employee')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
]
