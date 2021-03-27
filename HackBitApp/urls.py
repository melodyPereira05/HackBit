from django.urls import path
from  . import views

app_name='HackBitApp'

urlpatterns = [
    
     path('companies/',views.allcompany, name="all-company"),

    
]