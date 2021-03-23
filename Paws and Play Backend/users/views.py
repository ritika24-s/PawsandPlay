from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from django.views.generic import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from rest_framework.response import Response
from rest_framework import status
from rest_framework.request import Request

from .models import *
from .serializers import *


 
class userloginAPIView(APIView):

    permission_classes = [AllowAny]
    def post(self,request, format=None):
        try:
            user_email_id = request.data['user_email_id']
            is_present = user_login_details.objects.get(user_email_id = user_email_id)    # club these two lines
            serializer = userloginSerializer(is_present)
            if is_present:
                return Response({'id':serializer.data['id']}, status=status.HTTP_201_CREATED)
            else:
                return Response("Data not found", status=status.HTTP_404_NOT_FOUND)
        except:
            serializer = userloginSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'id':serializer.data['id']}, status=status.HTTP_201_CREATED)
            return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)
 
        
####################### appointments ##########################################

#class AppointmentListView(ListView):
#    """Shows users a list of appointments"""

#    model = Appointment


#class AppointmentDetailView(DetailView):
#    """Shows users a single appointment"""

#    model = Appointment


#class AppointmentCreateView(SuccessMessageMixin, CreateView):
#    """Powers a form to create a new appointment"""

#    model = Appointment
#    fields = ['name', 'phone_number', 'time', 'time_zone']
#    success_message = 'Appointment successfully created.'


#class AppointmentUpdateView(SuccessMessageMixin, UpdateView):
#    """Powers a form to edit existing appointments"""

#    model = Appointment
#    fields = ['name', 'phone_number', 'time', 'time_zone']
#    success_message = 'Appointment successfully updated.'


#class AppointmentDeleteView(DeleteView):
#    """Prompts users to confirm deletion of an appointment"""

#    model = Appointment
#    success_url = reverse_lazy('list_appointments')