"""demoproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from . import settings
from django.conf.urls.static import static 
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('notifications/', include('notify.urls',namespace = 'notifications')),
    ## for adoption ##
   
    path('api/adoption/', include('webapp.api.urls',namespace = 'adoption-api')),
    path('adoption/', include('webapp.urls',namespace = 'adoption')),

    ## for vendor ##
    path('api/vendor/', include('vendor.api.urls',namespace = 'vendor-api')),
    path('vendor/', include('vendor.urls',namespace = 'vendor')),

    ## for user ##
    path('user/', include('users.urls',namespace = 'user')),
    path('api/user/', include('users.api.urls',namespace = 'user-api')),

    ## for playdate ##
    path('playdate/', include('playdate.api.urls',namespace = 'playdate-api')),
    
]

        
if settings.DEBUG:
        urlpatterns += static(settings.STATIC_URL,
                              document_root=settings.STATIC_ROOT)
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
