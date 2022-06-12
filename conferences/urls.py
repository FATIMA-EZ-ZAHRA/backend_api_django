from django.urls import path 
from conferences import views

# define the urls
urlpatterns = [
    path('conferences/', views.conferences),
    path('conferences/<int:pk>/', views.conference_detail),
    path('conferenciers/', views.conferenciers),
]