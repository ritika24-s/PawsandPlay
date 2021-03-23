
#from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *

app_name = "users-api"


urlpatterns = [
    
########################### urls link for questionnaire ########################################
   path('questionnaire/request/',adoptionSaveView.as_view(),name ='question-request'),
   path('questionnaire/',questionnaireListAPIView.as_view()),
   path('questionnaire/create/',questionnaireCreateUpdateAPIView.as_view()),
   path('questionnaire/<user_id>/delete/',questionnaireDestroyAPIView.as_view()),
   path('questionnaire/<user_id>/',questionnaireRetrieveAPIView.as_view(),name ='questionnaire-detail'),
   #path('<user_id>/edit/',questionnaireCreateUpdateAPIView.as_view(),name ='questionnaire-update')
 
########################### urls link for pet ########################################
   #path('pet/request/',adoptionSaveView.as_view(),name ='request'),
   path('pet/',petListAPIView.as_view()),
   path('pet/create/',petCreateUpdateAPIView.as_view()),
   #path('pet/<user_id>/delete/',questionnaireDestroyAPIView.as_view()),
   path('pet/<user_id>/',petRetrieveAPIView.as_view(),name ='pet-detail'),
   #path('<user_id>/edit/',questionnaireCreateUpdateAPIView.as_view(),name ='questionnaire-update')
 
########################### urls link for owner ########################################
   #path('owner/request/',adoptionSaveView.as_view(),name ='request'),
   path('owner/',ownerListAPIView.as_view()),
   path('owner/create/',ownerCreateUpdateAPIView.as_view()),
   #path('owner/<user_id>/delete/',questionnaireDestroyAPIView.as_view()),
   path('owner/<pk>/',ownerRetrieveAPIView.as_view(),name ='owner-detail'),
   #path('<user_id>/edit/',questionnaireCreateUpdateAPIView.as_view(),name ='questionnaire-update')
    

]

