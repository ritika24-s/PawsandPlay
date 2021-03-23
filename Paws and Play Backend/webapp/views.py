from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import *
from vendor.models import vendor
from users.models import *
from .forms import applicationUpdateForm


def home(request):
    context = {
        'posts': adoption.objects.all()
    }
    return render(request, 'webapp/adoption_list.html', context)



class adoptionListView(ListView):
    def get_queryset(self):
        #import pdb
        #pdb.set_trace()
        self.vendor = get_object_or_404(vendor, user = self.request.user)
        adoption_obj = adoption.objects.filter(pet_vendor=self.vendor)
        #if not adoption_obj:
        #    return redirect('adoption:create')
        #else:
        return adoption.objects.filter(pet_vendor=self.vendor)
    
    template_name = 'webapp/adoption_list.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'adoption'
    ordering = ['vendor_timestamp']


class adoptionDetailView(DetailView):
    model = adoption


class adoptionCreateView(LoginRequiredMixin, CreateView):
    model = adoption
    fields = ['pet_name', 'pet_type', 'pet_breed','pet_gender','pet_age','pet_color','pet_count','pet_images','pet_bio',
              'pet_adoption_status']
    #success_url = reverse_lazy('adoption:detail')

    def form_valid(self, form):
        #import pdb
        #pdb.set_trace()
        self.vendor = get_object_or_404(vendor, user = self.request.user)
        form.instance.pet_vendor = self.vendor
        form.instance.pet_point_of_contact = self.vendor.vendor_contact
        form.instance.pet_email_id = self.request.user.email
        form.instance.pet_adoption_location = self.vendor.pet_adoption_location
        form.instance.pet_location_longitude = self.vendor.pet_location_longitude
        form.instance.pet_location_latitude = self.vendor.pet_location_latitude
        form.instance.pet_adoption_centre_logo = self.vendor.pet_adoption_centre_logo
        print(form.cleaned_data)
        #email id, contact, location
        return super().form_valid(form)


class adoptionUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = adoption
    fields = '__all__'
    pk = 'pet_id'

    def form_valid(self, form):
        form.instance.pet_vendor.user = self.request.user #.username
        print(form.cleaned_data)
        return super().form_valid(form)

    def test_func(self):
        adoption = self.get_object()
        if self.request.user == adoption.pet_vendor.user:
            return True
        return False


class adoptionDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = adoption
    success_url = reverse_lazy('adoption:list')
    pk = 'pet_id'

    def test_func(self):
        #import pdb
        #pdb.set_trace()
        adoption = self.get_object()
        if self.request.user == adoption.pet_vendor.user:
            return True
        return False

######################################################################## vendor - user #########################################################


class adoptionrequestListView(ListView):
    #def get_object(self, pk):
    #    return adoption.objects.get(pk=pk)

    def get_queryset(self):
        #import pdb
        #pdb.set_trace()
        self.adoption = adoption.objects.get(pet_id=self.kwargs['pk'])
        #self.adoption_request = get_object_or_404(adoption_request, pet = self.adoption)
        #self.user_login_details = get_object_or_404(user_login_details, id = self.adoption_request.user.id)
        return adoption_request.objects.filter(pet = self.adoption)
        #return user_login_details.objects.filter(id=self.adoption_request.user.id)
    
    template_name = 'webapp/user_list.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'adoption_request'
    ordering = ['requested_at']
         
        #to write in html to get count of users
        #return adoption_request.objects.filter(pet = self.adoption).count()


class adoption_requestUpdateView(LoginRequiredMixin, UpdateView):
    form_Class = applicationUpdateForm
    template_name = 'webapp/adoption_request_form.html'
    fields = ['application_status']
    #import pdb
    #pdb.set_trace()

    
    def form_valid(self, form):
        #form.instance.application_status = self.request.data #.username
        form.instance.pet.pet_vendor.user = self.request.user
        print(form.cleaned_data)
        return super().form_valid(form)

    def get_object(self):
        return get_object_or_404(adoption_request,id=self.kwargs['pk'])

    #success_url = reverse_lazy('adoption:request')
    def get_success_url(self):
        return reverse('adoption:request', kwargs={'pk': self.kwargs['pk']})

    #def test_func(self):
    #    obj = self.get_object()
    #    if self.request.user == obj.pet.pet_vendor.user:
    #        return True
    #    return False
         
    
class questionDetailView(DetailView):
    #def get_object(self, pk):
    #    return adoption.objects.get(pk=pk)

    def get_queryset(self):
        #import pdb
        #pdb.set_trace()
        return questionnaire.objects.filter(id = self.kwargs['pk'])
        
    
    template_name = 'webapp/user_detail.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'questionnaire'
         
        #to write in html to get count of users
        #return adoption_request.objects.filter(pet = self.adoption).count()

class notificationsListView(ListView):
    def get_queryset(self):
        #import pdb
        #pdb.set_trace()
        #self.adoption = adoption.objects.filter(pet_vendor=self.request.user.vendor).first()
        return adoption_request.objects.all()
    
    template_name = 'vendor/notifications.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'adoption_request'
    ordering = ['requested_at']
