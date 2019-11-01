#/users/models.py

from django.contrib.auth.models import AbstractBaseUser
from django.db import models
#from django.contrib.auth.models import User

class CustomUser(AbstractBaseUser):
	username = models.CharField(max_length=10, unique=True)
	email = models.EmailField(verbose_name='email address', max_length=255,unique=True,)
	
	#password?
	
	date_of_birth = models.DateField(null=True,blank=True)
	status = models.BooleanField(default=True) #True for Worker, False for Client
	work_field = models.TextField(null=True,blank=True)
	visibile = models.BooleanField(default=True) #visible if no complains
	available = models.BooleanField(default=True) #True if available, false otherwise.
	
	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = []
	
	def __str__(self):
		return self.email
