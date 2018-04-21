from django.contrib import admin

# Register your models here.
from howler_app.models import UserProfile,Howler

admin.site.register(UserProfile)
admin.site.register(Howler)

