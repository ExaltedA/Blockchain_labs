
from django.urls import path, include

from rootapp import views

urlpatterns = [

    path('', views.root, name = 'root'),
]
