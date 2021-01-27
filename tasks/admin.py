from django.contrib import admin
from . import models



@admin.register(models.TodoItem)
class TodoItemAdmin(admin.ModelAdmin):
    list_display=('description', 'is_completed', 'created')



# Register your models here.
