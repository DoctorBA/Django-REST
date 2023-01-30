from django.contrib import admin
from .models import Author


@admin.register(Author)
class PostAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'date_of_birth', 'date_of_death']
