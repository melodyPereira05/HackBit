from django.contrib import admin
from .models import Template, Coverlettertemplate, Cvtemplate
# Register your models here.

admin.site.register(Template)
admin.site.register(Cvtemplate)
admin.site.register(Coverlettertemplate)