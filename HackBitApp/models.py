from django.db import models
from datetime import datetime
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone



class Company(models.Model):
    name=models.CharField(unique=True,max_length=200,db_index=True)
    photo=models.ImageField(upload_to='photos/company/')
    slug=models.SlugField(max_length=200,unique=True)
    
    # def get_absolute_url(self):
    #     return reverse('HackBitApp:company_data',args=[self.slug])
    
    
    class Meta:        
        ordering=('name',)
        verbose_name='company'
        verbose_name_plural='companies'
    
    def __str__(self):
        return self.name


class Topquestion(models.Model):
    LEVEL = (
    
        ('Easy', 'EASY'),
        ('Medium', 'MEDIUM'),
        ('Hard', 'HARD'),

    )
    question_name=models.CharField(max_length=200,db_index=True)
    slug=models.SlugField(max_length=200,db_index=True,null=True,blank=True)
    link = models.URLField(max_length=200)
    difficulty=models.CharField(max_length=10,choices=LEVEL, default='Easy')
    companyTags=models.TextField(max_length=255)
    score=models.IntegerField(default=0)
    timetaken = models.CharField(max_length=150)
    
    def get_absolute_url(self):
        return reverse('HackBitApp:top-questions',args=[self.id])
    
    
    class Meta:        
        ordering=('question_name',)
        index_together=(('id','slug'),)
        verbose_name='topquestion'
        verbose_name_plural='topquestions'
    def __str__(self):
        return self.question_name
    
    
class Todolist(models.Model):
    LEVEL = (
    
        ('Easy', 'EASY'),
        ('Medium', 'MEDIUM'),
        ('Hard', 'HARD'),

    )
    
    question_name=models.CharField(max_length=200)
    slug=models.SlugField(max_length=200,db_index=True)
    link = models.URLField(max_length=200)
    difficulty=models.CharField(max_length=10,choices=LEVEL, default='Easy')
    companyTags=models.TextField(max_length=255)
    slug=models.SlugField(max_length=200,db_index=True,null=True,blank=True)
    question_id=models.IntegerField()
    Wishlisted_date=models.DateTimeField(default=datetime.now,blank=True)
    user_id=models.IntegerField(blank=False)
    
    def get_absolute_url(self):
        return reverse('HackBitApp:top-questions',args=[self.lot_id,self.slug])
    def __srt__(self):
        return self.question_name
    
    
class Data(models.Model):
    users = models.ManyToManyField(User)
    popular = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.popular