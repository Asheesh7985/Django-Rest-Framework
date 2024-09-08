
from django.contrib import admin
from django.urls import path,include
from rest_framework.routers  import DefaultRouter
from restApp import views
from restApp.auth import CustomAuthToken


router = DefaultRouter()

router.register('employee-api', views.EmployeeApiView,basename='Employee')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls',namespace='rest_framework')),
    path('getToken/', CustomAuthToken.as_view())
]