from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class RegistrationModel(models.Model):
	user = models.OneToOneField(User,on_delete = models.CASCADE)

	state = models.CharField(max_length=200)
	city = models.CharField(max_length=20)



	def __str__(self):
		return self.user.username

