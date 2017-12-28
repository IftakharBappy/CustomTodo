from django.contrib import admin
from .models import Todo


class TodoAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created')
    list_filter = ('created', 'name')
    search_fields = ('name',)
    prepopulated_fields = {'description': ('name',)}

    def get_queryset(self, request):
        queryset = super(TodoAdmin, self).get_queryset(request)
        queryset = queryset.order_by('name')
        return queryset


admin.site.register(Todo, TodoAdmin)


