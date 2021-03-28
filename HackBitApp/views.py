from django.shortcuts import render,get_object_or_404,redirect
from django.contrib import messages
from .implement import get_question,easy_question,medium_question,hard_question,getps
from .companyinfo import getreviews,getvalues
from .interview import get_experience
from .models import Data,Company,Topquestion,Todolist,Roadmap,Skill
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

def companydata(request,company_name):
    context={
        "company_name":company_name
    }
    return render(request,'company_data.html',context)
    

def practice(request,company_name):
    print(company_name)
    data=get_question(company_name)
    
    easy=easy_question(data)
    medium=medium_question(data)
    hard=hard_question(data)
    easyL=[]
    for elem in easy:
        easyL.append(elem)
        
    mediumL=[]
    for elem in medium:
        mediumL.append(elem)
        
    hardL=[]
    for elem in hard:
        hardL.append(elem)
    
    
    
    context={
       "easy":easyL,
       "medium":mediumL,
       "hard":hardL,
       "company_name":company_name
       
        } 
   
    return render(request, 'company-questions.html', context)
    

def roadmap(request,company_name):   
   roadmap=get_object_or_404(Roadmap,                          
                          company_name=company_name,
                          )
   roadmapl=[]
   if roadmap:
       roadmapl.append(roadmap.photo1)
       roadmapl.append(roadmap.photo2)
       roadmapl.append(roadmap.photo3)
       
       
   context={
       "roadmap":roadmapl
   }
   return render(request, 'roadmap.html', context)

def softskill(request,company_name):
    softskills=Skill.objects.all()    
    context={
        "skills":softskills,
    }
    return render(request, 'softskills.html', context)


def resume(request,company_name):
    resume="get from sukhada"
   
    return render(request, 'resume.html', context)


def interviewexp(request,company_name):
    interviewexp=get_experience(company_name)
    context={
        'interviewexp':interviewexp,
        'company_name':company_name
    }   
    return render(request, 'interviewexp.html', context)

def companyinfo(request,company_name):
    companyinfo_value=getvalues(company_name)
    companyinfo_reviews=getreviews(company_name)
   
    context={
        "value":companyinfo_value,
        "reviews":companyinfo_reviews,
        "company_name":company_name,
    }
    
    return render(request, 'companyinfo.html', context)

def allcompany(request):
    companyList=Company.objects.all()    
    context={
        "company_name":companyList,
    }
    
    return render(request, 'company_names.html', context)
    
    
    
def question(request,ques):    
    quez="https://www.geeksforgeeks.org/"+ques+'/'
    #print(quez)
    ps_and_eg, img, tags = getps(quez)
    context={
        "ps_eg":ps_and_eg,
        "img":img,
        "tags":tags
    }     
    return render(request,'question_detail.html',context)


