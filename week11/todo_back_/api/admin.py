from django.contrib import admin
from .models import TaskList, Task

admin.site.register(Task)
admin.site.register(TaskList)
# Register your models here.
