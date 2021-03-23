from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static 
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from django.contrib.auth import views as auth_views
from .views import *

app_name = "adoption"

urlpatterns = [
    path('create/',adoptionCreateView.as_view(), name = 'create'),
    path('<pk>/delete/',adoptionDeleteView.as_view(), name = 'delete'), 
    path('<pk>/',adoptionDetailView.as_view(), name = 'detail'), 
    path('',adoptionListView.as_view(),name = 'list'), 
    path('<pk>/update/',adoptionUpdateView.as_view(),name='update'), 
    path('<pk>/request/',adoptionrequestListView.as_view(),name = 'request'),
    path('<pk>/changestatus/',adoption_requestUpdateView.as_view(),name ='changestatus'),
    path('<pk>/detail/',questionDetailView.as_view(), name = 'userdetail')

    ]