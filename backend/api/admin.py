from django.contrib import admin
from .models import Todo

class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'created_at', 'updated_at')  # Display these fields in the list view
    search_fields = ('title', 'description')  # Add search functionality on title and description

admin.site.register(Todo, TodoAdmin)