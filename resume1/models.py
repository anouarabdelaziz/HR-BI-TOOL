from django.db import models
from django.contrib.auth.models import models

class Recruit(models.Model):
    name = models.CharField(blank=False, max_length=200, null=True)
    Description = models.TextField(blank=False, null=True)
    
    def __str__(self):
        return self.name


class Apply(models.Model):
    STATUS = (
            ('1', 'less then one year'), 
            ('3', 'between two and three years'),
            ('5', 'between three and five years'),
            ('7', 'between five and ten years'),
            ('10', 'more then ten years'),
            )
    FullName = models.CharField(max_length=50, blank=False, null=True)
    experience = models.CharField(max_length = 50, null=True, choices=STATUS)
    Cv = models.FileField(upload_to = 'media/pdfs/')
    date_created = models.DateTimeField(auto_now_add=True, null=True)
   
    def __str__(self):
        return self.FullName


class Comp(models.Model):
    STATUS = (
            ('REQUIRED' , '1'), 
            ('SECONDARY' , '2'),
            ('PLUS' , '3'),
            )
    recruit = models.ForeignKey(Recruit, null=True, on_delete = models.SET_NULL)
    name = models.CharField(max_length=200, null=True)
    importance = models.IntegerField(choices=((("REQUIRED"), 1),(("SECONDARY"), 2),(("PLUS"), 3)), default="REQUIRED")    
    
    def __str__(self):
        return self.name

