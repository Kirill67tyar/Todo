from django.contrib import admin
from .models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'birthdate', 'avatar']

# admin.site.register(ProfileAdmin) # можно так зарегистрировать в админку наш класс
# Register your models here.
