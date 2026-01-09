from django.contrib import admin
from .models import Habit

# Register your models here.
@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    model = Habit
    list_display = ['name', 'description', 'is_active']
    search_fields = ['name', 'description']

