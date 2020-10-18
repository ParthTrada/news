from django.db import models
#from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
# author = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)
# author = models.ForeignKey(User, on_delete=models.CASCADE)
class Entry(models.Model):
	title = models.CharField(max_length=50, null=True, blank=True)
	text = models.TextField(null=True, blank=True)
	date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
	author = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)
	

	class Meta:
		verbose_name_plural = "entries"

	def __str__(self):
		return self.title + ' | ' + str(self.author)

	def get_absolute_url(self):
	    return reverse('/blog/', args=(str(self.id)))	


		 
# date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
	