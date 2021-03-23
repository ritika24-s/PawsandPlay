from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *
from webapp.api.views import adoption_relListView, adoption_relDetailView,adoptionrequestedListAPIView

app_name = "users"


urlpatterns = [
   path('login/',userloginAPIView.as_view()),
   path('choose/',adoption_relListView.as_view()),
   path('choose/<pk>/',adoption_relDetailView.as_view()),
   path('request-list/',adoptionrequestedListAPIView.as_view()),
   #path('appointment/new/', AppointmentCreateView.as_view(), name='new_appointment'),
   #path('appointment/', AppointmentListView.as_view(), name='list_appointments'),
   #path('appointment/<pk>/delete/', AppointmentDeleteView.as_view(), name='delete_appointments'),
   #path('appointment/<pk>/update/', AppointmentUpdateView.as_view(), name='update_appointments'),

     
]

