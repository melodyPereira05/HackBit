from django.shortcuts import render,get_object_or_404,redirect
from django.core.paginator import Paginator
from .models import Template, Coverlettertemplate, Cvtemplate
# Create your views here.

def show_resume(request):
    context = {}
    context["temp"] = Template.objects.all()
    print(context)
    return render(request,'resumetemplates.html', context)

def show_cv(request):
    context = {}
    context["temp"] = Cvtemplate.objects.all()
    print(context)
    return render(request,'cvtemplates.html', context)

def show_coverletter(request):
    context = {}
    context["temp"] = Coverlettertemplate.objects.all()
    print(context)
    return render(request,'coverlettertemplates.html', context)

def howtowritearesume(request):
    return render(request, 'resumebuilding.html')