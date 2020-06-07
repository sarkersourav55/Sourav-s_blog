from django.db import models
from django.urls import reverse
class sub(models.Model):
	email = models.EmailField()
	time = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return self.email


        
    
