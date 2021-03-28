from django.urls import path
from  . import views

app_name='Resume'

urlpatterns = [
    path('resumetemplates/',views.show_resume,name="showresume"),
    path('cvtemplates/',views.show_cv,name="showcv"),
    path('coverlettertemplates/',views.show_coverletter,name="showcoverletter"),
    path('howtowritearesume/',views.howtowritearesume,name="howtowritearesume"),
]