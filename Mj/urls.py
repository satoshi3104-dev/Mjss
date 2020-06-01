from Mjss.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]