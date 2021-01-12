from . import views
from django.urls import path
urlpatterns = [
    path('index', views.index, name='index'),
    path('participant', views.participant, name='participant'),
    path('detail<int:id>', views.detail, name='detail')
]