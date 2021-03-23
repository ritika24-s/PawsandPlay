from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateAPIView, DestroyAPIView, RetrieveAPIView
from django.db.models import Q
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from ..models import *
from .serializers import *
#from .permissions import IsOwnerOrReadOnly
#from .pagination import *


########################### Views for vendor ########################################

class vendorListAPIView(ListAPIView):
    queryset = vendor.objects.all()
    serializer_class = vendorListSerializer
    permission_classes = [AllowAny]
    #pagination_class = vendorOffsetLimitPagination
    #pagination_class = vendorPageNumberPagination

    #add filters
    # filter_backends = [SearchFilter,OrderingFilter]            for showing in asc/desc order
    filter_backends = [SearchFilter,DjangoFilterBackend]
    #search_fields = ['pet_breed','pet_type','pet_gender']
    #filterset_fields = ['pet_breed','pet_type','pet_gender']

class vendorRegisterAPIView(APIView):
    permission_classes = [IsAdminUser]
    def post(self, request, format='json'):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                token = Token.objects.create(user=user)
                json = serializer.data
                json['token'] = token.key
                return Response(json, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class vendorDestroyAPIView(DestroyAPIView):
    queryset = vendor.objects.all()
    serializer_class = vendorRetrieveSerializer
    #lookup_field = 'vendor_username'
    permission_classes = [IsAdminUser]


class vendorRetrieveAPIView(RetrieveAPIView):
    queryset = vendor.objects.all()
    serializer_class = vendorRetrieveSerializer
    #lookup_field = 'vendor_username'
    permission_classes = [IsAuthenticatedOrReadOnly]


class vendorUpdateAPIView(RetrieveUpdateAPIView):
    queryset = vendor.objects.all()
    serializer_class = vendorUpdateSerializer
    #lookup_field = 'vendor_username' 
    permission_classes = [IsAdminUser]


############################################# registration api ###################################################

