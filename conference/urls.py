
from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    
    # for amphitheatres
    path('api/', include('amphitheatres.urls')),

      # for participants
    path('api/', include('participants.urls')),
    # for admin side

      # for conferences
    path('api/', include('conferences.urls')),


    # for admin side
    path('admin/', admin.site.urls),
]