from django.contrib import admin
from .models import Data,Company,Topquestion,Todolist,Roadmap,Skill
# Register your models here.
admin.site.register(Data)
admin.site.register(Todolist)
admin.site.register(Company)
admin.site.register(Topquestion)
admin.site.register(Roadmap)
admin.site.register(Skill)