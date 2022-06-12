from django.urls import path 
from amphitheatres import views

# define the urls
urlpatterns = [
    path('amphitheatres/', views.amphitheatres),
    path('amphitheatres/<int:pk>/', views.amphitheatre_detail),
]