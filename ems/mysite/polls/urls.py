from django.urls import path

from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('form1',views.form1, name='form1'),
    path('graphs',views.graphs, name='graphs')
]