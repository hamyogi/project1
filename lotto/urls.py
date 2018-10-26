from django.urls import path
from . import views


urlpatterns = [
 path('', views.index),
 path('form', views.post),
 path('detail', views.detail),
 path('detail/<int:num>', views.detail2),
 path('join', views.join),
 path('id_check', views.id_check),
]