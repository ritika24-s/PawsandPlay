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
from webapp.models import *
from .serializers import *
from .permissions import IsOwnerOrReadOnly
from .pagination import *


########################### Views for owner ########################################

class ownerListAPIView(ListAPIView):
    #queryset = owner.objects.filter(user_login_details__id = request.data['user_id'])
    serializer_class = ownerListSerializer

    filter_backends = [SearchFilter]
    #search_fields = ['user_fullname','user_emailid','user_contact_number']
    pagination_class = questionnaireOffsetLimitPagination

    def get_queryset(self):
        #import pdb
        #pdb.set_trace()
        self.user = get_object_or_404(user_login_details, id = request.data['user_id'])
        return owner.objects.filter(user=self.user)


class ownerRetrieveAPIView(RetrieveAPIView):
    queryset = owner.objects.all()
    serializer_class = ownerRetrieveSerializer 

class ownerCreateUpdateAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self,request, format=None):
        
        user_ids = user_login_details.objects.get(id = request.data['user_id'])  
        try:
            owner_obj = owner.objects.get(user_id=user_ids)
            if owner_obj:
                update_obj = owner.objects.filter(user_id=user_ids)
                update_obj.__dict__.update(request.data)
                return Response(request.data['user_id'],status=status.HTTP_200_OK)
            else:
                return Response("Data not found", status=status.HTTP_404_NOT_FOUND)
        except:
            serializer = ownerCreateUpdateSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(request.data['user_id'],status=status.HTTP_201_CREATED)
            return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)


########################### Views for pet ########################################

class petListAPIView(ListAPIView):

    serializer_class = petListSerializer
    pagination_class = questionnaireOffsetLimitPagination

    def get_queryset(self):
        self.user = get_object_or_404(user_login_details, id = request.data['user_id'])
        self.owner = owner.objects.filter(user=self.user)
        return pet.objects.filter(pet_owner=self.owner)


class petRetrieveAPIView(RetrieveAPIView):
    queryset = pet.objects.all()
    serializer_class = petRetrieveSerializer 


class petCreateUpdateAPIView(APIView):
    
    def post(self,request, format=None):
        
        try:
            pet_obj = pet.objects.get(pet_id=request.data['pet_id'])
            if pet_obj:
                update_obj = pet.objects.filter(pet_id=request.data['pet_id'])
                update_obj.__dict__.update(request.data)
                return Response(request.data['pet_id'],status=status.HTTP_200_OK)
            else:
                return Response("Data not found", status=status.HTTP_404_NOT_FOUND)
        except:
            serializer = petCreateUpdateSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(request.data['pet_id'],status=status.HTTP_201_CREATED)
            return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)

########################### Views for questionnaire ########################################

class questionnaireListAPIView(ListAPIView):

    queryset = questionnaire.objects.all()
    serializer_class = questionnaireListSerializer
    permission_classes = [IsOwnerOrReadOnly]

    #add filters
    # filter_backends = [SearchFilter,OrderingFilter]            for showing in asc/desc order
    filter_backends = [SearchFilter]
    search_fields = ['user_fullname','user_emailid','user_contact_number']
    pagination_class = questionnaireOffsetLimitPagination

    #def list(self, request):
    #    # Note the use of `get_queryset()` instead of `self.queryset`
    #    queryset = questionnaire.objects.all()
    #    serializer = questionnaireListSerializer(queryset)
    #    return Response(serializer.data)
    #pagination_class = questionnairePageNumberPagination

     #def get_queryset(self):
     #   #import pdb
     #   #pdb.set_trace()
     #   self.questionnaire = get_object_or_404(questionnaire, user_id = self.request.user)
     #   #return adoption.objects.all()
     #   return questionnaire.objects.filter(pet_vendor=self.vendor)


    #def get_queryset(self, *args, **kwargs):
    #    #queryset_list = super(adoptionListAPIView, self).get_queryset(*args, **kwargs) 
    #    queryset_list = questionnaire.objects.all()
    #    query = self.request.GET.get("q")
    #    if query:
    #        queryset_list = queryset_list.filter(
    #            Q(user_fullname = query)|
    #            Q(user_emailid = query)|
    #            Q(user_contact_number = query)
    #            ).distinct
    #    return queryset_list


class questionnaireCreateUpdateAPIView(APIView):
    #queryset = questionnaire.objects.all()
    #serializer_class = questionnaireCreateUpdateSerializer
    ##create customized permission classes
    permission_classes = [AllowAny]

    #def perform_create(self, serializer):
    #    serializer.save(user_id = self.)
    def post(self,request, format=None):
        
        user_ids = user_login_details.objects.get(id = request.data['user_id'])  
        #serializer = userloginSerializer(is_present)
        try:
            que_obj = questionnaire.objects.get(user_id=user_ids)
            if que_obj:
                update_obj = questionnaire.objects.filter(user_id=user_ids)
                update_obj.__dict__.update(request.data)
                return Response(status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        except:
            serializer = questionnaireCreateUpdateSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_201_CREATED)
        

    
class questionnaireDestroyAPIView(DestroyAPIView):
    queryset = questionnaire.objects.all()
    serializer_class = questionnaireRetrieveSerializer 
    #lookup_field = 'user_id'
    permission_classes = [IsAdminUser]


class questionnaireRetrieveAPIView(RetrieveAPIView):
    queryset = questionnaire.objects.all() #filter(user_id = user_login_details.id)
    serializer_class = questionnaireRetrieveSerializer 
    lookup_field = 'user_id'
    permission_classes = [IsOwnerOrReadOnly]


#class questionnaireUpdateAPIView(RetrieveUpdateAPIView):
#    queryset = questionnaire.objects.all() #filter(user_id = user_login_details)
#    serializer_class = questionnaireCreateUpdateSerializer 
#    #lookup_field = 'user_id'
#    permission_classes = [IsOwnerOrReadOnly]

#    def perform_update(self, serializer):
#        #if self.user_id == user_login_details   check this condition
#        serializer.save(user_id = self.user_login_details)
#        # email send_email django feature to be introduced later

########################################################## adoption request model views #############################################################


class adoptionSaveView(APIView):
    permission_classes = [AllowAny]
    def post(self,request, format=None):
        user_obj = user_login_details.objects.get(id = request.data['user_id'])
        que_obj = questionnaire.objects.get(user_id = user_obj)
        pet_obj = adoption.objects.get(pet_id = request.data['pet_id'])
        create_obj = adoption_request.objects.create(user = user_obj,question = que_obj,pet = pet_obj)
        return Response(status = status.HTTP_200_OK)




    