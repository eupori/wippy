from django.contrib import admin
from nrise_app.models import(
	User,
	Session,
)
# Register your models here.
admin.site.register(User)
admin.site.register(Session)