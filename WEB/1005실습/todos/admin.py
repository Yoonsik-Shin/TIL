from django.contrib import admin
from .models import Todos

# Register your models here.
class TodoAdmin(admin.ModelAdmin):
    fields = ['title']

admin.site.register(Todos, TodoAdmin)