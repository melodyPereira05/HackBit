from django.contrib import admin
from .models import Data,Company,Topquestion,Todolist
# Register your models here.
admin.site.register(Data)
admin.site.register(Todolist)
admin.site.register(Company)
admin.site.register(Topquestion)