from django.db import models

# Create your models here.

class User(models.Model):
	user_id = models.CharField(max_length=100)
	password = models.CharField(max_length=64)
	lastest_logout = models.DateTimeField(null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
	is_active = models.BooleanField(default=True)


class Session(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="user_id")
	ip_address = models.CharField(max_length=100, null=True, blank=True)
	logout_at = models.DateTimeField(null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)