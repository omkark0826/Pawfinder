from django.urls import path
from . import views

urlpatterns = [
    path('', views.animal_list, name='animal_list' ),
    path('about/', views.about, name='about'),
    path('animal/<int:pk>/', views.animal_detail, name= 'animal_detail')
]

