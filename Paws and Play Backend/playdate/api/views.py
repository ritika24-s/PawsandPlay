from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateAPIView, DestroyAPIView, RetrieveAPIView
from django.db.models import Q
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework import status
from ..models import *
from users.models import *
from .serializers import *
from .permissions import IsOwnerOrReadOnly
from .pagination import *


########################################################## like views #############################################################


class likeCreateView(APIView):
    permission_classes = [AllowAny]
    def post(self,request, format=None):
        user1_obj = user_login_details.objects.get(id = request.data['user_id1'])
        user2_obj = user_login_details.objects.get(id = request.data['user_id2'])
        pet1_obj = adoption.objects.get(pet_id = request.data['pet_id1'])
        pet2_obj = adoption.objects.get(pet_id = request.data['pet_id2'])
        
        create_obj = like.objects.create(user1 = user1_obj,user2 = user2_obj,pet1 = pet1_obj,pet2 = pet2_obj, reaction=request.data['reaction'])
        return Response(status = status.HTTP_200_OK)




    