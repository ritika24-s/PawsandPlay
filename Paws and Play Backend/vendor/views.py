# Create your views here.
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404 , redirect
from django.contrib.auth import authenticate, get_user_model, login, logout

from .models import vendor
from .forms import *
from django.contrib.auth.decorators import login_required

def register_view(request):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    if request.method == 'POST':
        form = vendorRegisterForm(request.POST)     #vendor
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Your account has been created! You are now able to log in')
            return redirect('vendor/login')
    else:
        form = vendorRegisterForm()
    return render(request, 'vendor/register.html', {'form': form})


   
@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = vendorUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.vendor)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your account details have been updated!')
            return redirect('adoption:list')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = vendorUpdateForm(instance=request.user.vendor)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'vendor/profile.html', context)


