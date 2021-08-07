from django.contrib import admin
from .models import ToDo


class showCreated(admin.ModelAdmin):
    readonly_fields = ('created',)


admin.site.register(ToDo, showCreated)
