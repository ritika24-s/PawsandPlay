
#from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *

app_name = "vendor"


urlpatterns = [
    
########################### urls link for vendor ########################################

   path('',vendorListAPIView.as_view(),name ='list'),
   path('create/',vendorRegisterAPIView.as_view(),name ='create'),
   path('<pk>/delete/',vendorDestroyAPIView.as_view(),name ='delete'),
   path('<pk>/',vendorRetrieveAPIView.as_view(),name ='detail'),
   path('<pk>/edit/',vendorUpdateAPIView.as_view(),name ='update'),
      

]

