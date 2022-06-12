from django.urls import path 
from participants import views

# define the urls
urlpatterns = [
    path('participants/', views.participants),
    path('participants/<int:pk>/', views.participant_detail),
]