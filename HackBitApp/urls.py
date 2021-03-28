from django.urls import path
from  . import views

app_name='HackBitApp'

urlpatterns = [
    
    path('companies/',views.allcompany, name="all-company"),
    path('companies/<company_name>/',views.companydata, name="company_data"),
    path('<company_name>/resumebuild',views.resume, name="resumebuild"),
    path('<company_name>/practice',views.practice, name="practice"),
    path('<company_name>/softskill',views.softskill, name="softskill"),
    path('<company_name>/roadmap',views.roadmap, name="roadmap"),
    path('<company_name>/interviewexp',views.interviewexp, name="interviewexp"),
    path('<company_name>/companyinfo',views.companyinfo, name="companyinfo"),
    path('<ques>/',views.question, name="question"),
  
     
# {{ps_eg}}
#         {{img.url}}
#         {{tags}}
    
]