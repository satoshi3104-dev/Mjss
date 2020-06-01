from Mjss.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:num>', views.index, name='index'),
    path('find', views.find, name='find'),
]