from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404 , redirect

from .models import adoption
from .forms import *

def vendor_delete(request,pet_id = None):
    instance = get_object_or_404(adoption, pet_id=pet_id)
    instance.delete()
    messages.success(request, "Successfully deleted")
    return redirect("adoption:list")


def vendor_create(request):
    form = adoptionForm(request.adoption or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        #print form.cleaned_data.get("pet_name")
        instance.save()
        # message success
        messages.success(request, "Successfully Created")
        return HttpResponseRedirect(instance.get_absolute_url())
    #else:
    #    messages.error(request, "Not Successfully Created")
	# if request.method == "POST":
	# 	print "title" + request.POST.get("content")
	# 	print request.POST.get("title")
	# 	#Post.objects.create(title=title)
    context = {
		"form": form,
	}
    return render(request, "webapp/adoption_form.html", context)


def vendor_retrieve(request,pet_id):
    #instance = Post.objects.get(id=1)

	instance = get_object_or_404(adoption, pet_id=pet_id)
	context = {
		"title": instance.pet_name,
		"instance": instance,
	}
	return render(request, "webapp/adoption_detail.html", context)
    #return render(request,'vendor/register.html', {'form':form})    # api call


def vendor_list(request):
    #form = UserCreationForm()
    #return HttpResponse("<h1>Hello</h1>")
    #return render(request,'vendor/register.html', {'form':form})    # api call

    #loggedin_vendor = request.pet_adoption_centre_name

    queryset = adoption.objects.filter(user=request.user)
    context = {
        "adoption_list" : queryset,
		"title": "List"
	}

	# if request.user.is_authenticated():
	# 	context = {
	# 		"title": "My User List"
	# 	}
	# else:
	# 	context = {
	# 		"title": "List"
	# 	}

    return render(request, "webapp/adoption_list.html", context)
    #return render(request,'index.html', {'form':form})    # api call



def vendor_update(request, pet_id=None):
	instance = get_object_or_404(adoption, pet_id=pet_id)
	form = adoptionForm(request.adoption or None, request.FILES or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "<a href='#'>Item</a> Saved", extra_tags='html_safe')
		return HttpResponseRedirect(instance.get_absolute_url())

	context = {
		"title": instance.pet_name,
		"instance": instance,
		"form":form,
	}
	return render(request, "webapp/adoption_form.html", context)