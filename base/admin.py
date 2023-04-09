from django.contrib import admin

# Register your models here.

from .models import New, User, About

admin.site.register(New)
admin.site.register(User)
admin.site.register(About)
