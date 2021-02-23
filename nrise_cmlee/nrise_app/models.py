from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class User(User):
	lastest_logout = models.DateTimeField(null=True, blank=True),
	created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True),


class Session(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="user_id"),
	ip_address = models.CharField(max_length=100, null=True, blank=True),
	lastest_logout = models.DateTimeField(null=True, blank=True),
	created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True),