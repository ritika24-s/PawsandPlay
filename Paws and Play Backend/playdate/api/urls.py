from django.urls import path
#from rest_framework.urlpatterns import format_suffix_patterns
from .views import *

app_name = "playdate-api"


urlpatterns = [
    
########################### urls link for questionnaire ########################################
   path('',likeCreateView.as_view(),name ='like'),   

]

