from django.contrib import admin

# Register your models here.

from .models import New, User, About, Message, File, Event

admin.site.register(New)
admin.site.register(User)
admin.site.register(About)
admin.site.register(Message)
admin.site.register(File)
admin.site.register(Event)

