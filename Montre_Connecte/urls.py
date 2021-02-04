from . import views
from django.contrib import admin
from django.urls import path
urlpatterns = [

    path('', views.index, name='index'),
    path('participant', views.participant, name='participant'),
    path('detail<int:id>', views.detail, name='detail'),
    path('telechargement', views.telechargement, name='telechargement'),
    path('rapport', views.rapport, name='rapport'),
    path('admin/', admin.site.urls)
]
