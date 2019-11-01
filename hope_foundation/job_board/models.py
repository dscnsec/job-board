#/job_board/models.py

#from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.db import models

class CustomUser(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	username = models.CharField(max_length=10, unique=True)
	email = models.EmailField(verbose_name='email address', max_length=255,unique=True,)
	
	#password?
	
	date_of_birth = models.DateField()
	status = models.BooleanField(default=True) #True for Worker, False for User
	visibile = models.BooleanField(default=True) #visible if no complains
	available = models.BooleanField(default=True) #True if available, false otherwise.
	
	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['date_of_birth']
	
	def __str__(self):
		return self.email
