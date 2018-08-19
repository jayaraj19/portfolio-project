from django.urls import path
from jobs import views

app_name = 'jobs'

urlpatterns = [
    path('', views.index, name='index'),
]
