from xml.parsers.expat import model
from django.db import models

# Create your models here.
class Chat(models.Model):
    question = models.CharField(max_length=254)
    answer = models.TextField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.question