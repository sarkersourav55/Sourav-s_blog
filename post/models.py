from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from tinymce.models import HTMLField


User=get_user_model()

class author(models.Model):
	user=models.OneToOneField(User, on_delete=models.CASCADE)
	dp = models.ImageField()

	def __str__(self):
		return self.user.username


class category(models.Model):
	title = models.CharField(max_length=50)

	def __str__(self):
		return self.title

class post(models.Model):
	title= models.CharField(max_length=100)
	cat = models.ManyToManyField(category)
	overview = models.TextField()
	time = models.DateTimeField(auto_now_add=True)
	comment_count = models.IntegerField(default=0)
	author=models.ForeignKey(author,on_delete=models.CASCADE)
	featured = models.BooleanField(null=True)
	thumb = models.ImageField(null=True)
	view = models.IntegerField(default=0)
	content = HTMLField()
	previous=models.ForeignKey("self",related_name="previous_post",on_delete=models.SET_NULL,blank=True,null=True)
	nex=models.ForeignKey("self",related_name="next_post",on_delete=models.SET_NULL,blank=True,null=True)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('post',kwargs={'id':self.id})
