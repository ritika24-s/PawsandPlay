from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateAPIView, DestroyAPIView, RetrieveAPIView
from django.db.models import Q
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import *
from .serializers import *
from .permissions import IsOwnerOrReadOnly
from .pagination import *



########################### Views for adoption ########################################


class adoptionListAPIView(ListAPIView):
    serializer_class = adoptionListSerializer
    #queryset = adoption.objects.all()
    #queryset = adoption.objects.all().filter(pet_adoption_centre_name=self.request.pet_adoption_centre_name)
    permission_classes = [AllowAny]
    pagination_class = adoptionOffsetLimitPagination
    #pagination_class = adoptionPageNumberPagination

    #add filters
    # filter_backends = [SearchFilter,OrderingFilter]            for showing in asc/desc order
    filter_backends = [SearchFilter,DjangoFilterBackend]
    search_fields = ['pet_breed','pet_type','pet_gender']
    filterset_fields = ['pet_breed','pet_type','pet_gender']

    #def get_queryset(self, *args, **kwargs):
    #    #queryset_list = super(adoptionListAPIView, self).get_queryset(*args, **kwargs) 
    #    queryset_list = adoption.objects.all()
    #    query = self.request.GET.get("q")
    #    if query:
    #        queryset_list = queryset_list.filter(
    #            Q(pet_breed = query)|
    #            Q(pet_type = query)|
    #            Q(pet_gender = query)
    #            ).distinct
    #    return queryset_list
    def get_queryset(self):
        self.vendor = get_object_or_404(vendor, user = self.request.user)
        return adoption.objects.filter(pet_vendor=self.vendor)


class adoptionCreateAPIView(CreateAPIView):
    queryset = adoption.objects.all()
    serializer_class = adoptionCreateUpdateSerializer
    permission_classes = [IsAdminUser]

    #def perform_create(self, serializer):
    #    serializer.save(pet_adoption_centre_name = self.request.pet_adoption_centre_name)


class adoptionDestroyAPIView(DestroyAPIView):
    queryset = adoption.objects.all()
    serializer_class = adoptionRetrieveSerializer
    lookup_field = 'pet_id'
    permission_classes = [IsAdminUser]


class adoptionRetrieveAPIView(RetrieveAPIView):
    queryset = adoption.objects.all()
    serializer_class = adoptionRetrieveSerializer
    lookup_field = 'pet_id'
    permission_classes = [AllowAny]


class adoptionUpdateAPIView(RetrieveUpdateAPIView):
    queryset = adoption.objects.all()
    serializer_class = adoptionCreateUpdateSerializer
    lookup_field = 'pet_id' 
    permission_classes = [IsAdminUser]

################################################################################################################################################
############################################ for user app ################################################################################

class adoption_relListView(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        pet = adoption.objects.all()
        serializer = adoptionuserListSerializer(pet, many=True)
        return Response(serializer.data)


class adoption_relDetailView(APIView):
    permission_classes = [AllowAny]
    def get_object(self, pk):
        try:
            return adoption.objects.get(pk=pk)
        except adoption.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        pet = self.get_object(pk)
        serializer = adoptionuserRetrieveSerializer(pet)
        return Response(serializer.data)

class adoptionrequestedListAPIView(APIView):
    permission_classes = [AllowAny]
    def post(self, request, format=None):
        user_obj = user_login_details.objects.get(id = request.data['user_id'])
        adoption_list = adoption_request.objects.filter(user = user_obj)
        serializer = adoptionRequestListSerializer(adoption_list,many=True)
        return Response(serializer.data)


    