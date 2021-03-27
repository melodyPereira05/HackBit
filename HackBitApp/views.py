from django.shortcuts import render,get_object_or_404,redirect
from django.contrib import messages
from .implement import get_question,easy_question,medium_question,hard_question
from .models import Data,Company,Topquestion,Todolist
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.utils.safestring import mark_safe
import json
from django.core.mail import send_mail

#after clicking on a specific company

def popular_question(request):
    list = Data.objects.annotate(user_count=Count('users')).order_by('-user_count')
    return render(request, 'popular_question.html', {'list': datalist})


def company_data(request,company_name):
    data=get_question(company_name)
    easy=easy_question(data)
    medium=medium_question(data)
    hard=hard_question(data)
    
    context={
       "easy":easy,
       "medium":medium,
       "hard":hard
            }
   
    return render(request, 'company-questions.html', context)
    

def allcompany(request):
    companyList=Company.objects.all()
    
    context={
        "company_name":companyList,
    }
    
    return render(request, 'company_names.html', context)
    
    
    
    


