from django.contrib import admin

# Register your models here.

from .models import New, User

admin.site.register(New)
admin.site.register(User)