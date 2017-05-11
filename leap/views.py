from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import *

def index(request):
    return render(request, 'leap/index.html')

def redirect_create(request):
    return render(request, 'leap/create_class.html')

def createClass(request):
	newClass = LeapClass(
			classCode = request.POST['class_code'],
			className = request.POST['class_name'],
			capacity = request.POST['capacity']
		)
	newClass.save()
	return HttpResponseRedirect(reverse('leap:view_all'))

def viewClasses(request):
	classes = LeapClass.objects.all()
	context = {
		'classes': classes
	}
	return render(request, 'leap/view_classes.html', context)

def viewSingle(request, class_id):
	leapClass = get_object_or_404(LeapClass, pk=class_id)
	context = {
		'class': leapClass
	}
	return render(request, 'leap/view_single.html', context)

def redirect_enroll(request):
	classes = LeapClass.objects.all()
	context = {
		'classes': classes
	}
	return render(request, 'leap/enroll.html', context)

def enroll():
	return HttpResponseRedirect(reverse('leap:index'))