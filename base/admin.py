from django.contrib import admin

# Register your models here.

from .models import New, User, About, Message, File, Event, GroupNumber, Task, Subject

admin.site.register(New)
admin.site.register(User)
admin.site.register(About)
admin.site.register(Message)
admin.site.register(File)
admin.site.register(Event)
admin.site.register(GroupNumber)
admin.site.register(Task)
admin.site.register(Subject)

