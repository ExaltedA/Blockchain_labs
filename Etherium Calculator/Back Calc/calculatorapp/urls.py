
from django.urls import path, include

from calculatorapp import views

urlpatterns = [

    path('', views.index, name = 'index'),
    path('submitquery',views.submitquery,name='submitquery')
]
