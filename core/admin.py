from django.contrib import admin
from .models import Todo


class TodoAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created')
    list_filter = ('created', 'name')
    search_fields = ('name',)
    prepopulated_fields = {'description': ('name',)}


admin.site.register(Todo, TodoAdmin)


