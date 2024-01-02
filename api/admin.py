from django.contrib import admin
from api.models import Task

admin.site.register(Task)

class TaskAdmin(admin.ModelAdmin):
  list_display = ('id')


