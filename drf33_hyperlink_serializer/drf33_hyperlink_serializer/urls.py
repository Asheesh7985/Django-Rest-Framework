from django.contrib import admin
from django.urls import path,include
from restApp import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('student-api', views.StudentApiView,basename='Student')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    
]
