
#from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . views import *

app_name = "adoption"


urlpatterns = [
    
########################### urls link for adoption ########################################

   path('adoption/',adoptionListAPIView.as_view(),name ='adoptionList'),
   path('adoption/create/',adoptionCreateAPIView.as_view()),
   path('adoption/<pet_id>/delete/',adoptionDestroyAPIView.as_view()),
   path('adoption/<pet_id>/',adoptionRetrieveAPIView.as_view(),name ='adoption-detail'),
   path('adoption/<pet_id>/edit/',adoptionUpdateAPIView.as_view(),name ='adoption-update'),
  

]

