from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from restApp import views

router = DefaultRouter()

router.register('singe-api', views.SingerViewSet,basename='Singer')
router.register('song-api', views.SongViewSet,basename='Song')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls',namespace='rest_framework'))
]
