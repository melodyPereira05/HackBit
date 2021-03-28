from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Template(models.Model):
    template_type=models.CharField(max_length=200,db_index=True)
    template_name=models.CharField(unique=True,max_length=200,db_index=True)
    slug=models.SlugField(max_length=200,unique=True)
    stars = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    description = models.TextField(max_length=255)
    template_image = models.ImageField(upload_to='resumetemplates/')
    addtowishlist = models.BooleanField(default= False)

    def __str__(self):
        return self.template_name

class Cvtemplate(models.Model):
    template_type=models.CharField(max_length=200,db_index=True)
    template_name=models.CharField(unique=True,max_length=200,db_index=True)
    slug=models.SlugField(max_length=200,unique=True)
    stars = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    description = models.TextField(max_length=255)
    template_image = models.ImageField(upload_to='cvtemplates/')
    addtowishlist = models.BooleanField(default= False)

    def __str__(self):
        return self.template_name


class Coverlettertemplate(models.Model):
    template_type=models.CharField(max_length=200,db_index=True)
    template_name=models.CharField(unique=True,max_length=200,db_index=True)
    slug=models.SlugField(max_length=200,unique=True)
    stars = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    description = models.TextField(max_length=255)
    template_image = models.ImageField(upload_to='coverlettertemplates/')
    addtowishlist = models.BooleanField(default= False)

    def __str__(self):
        return self.template_name
