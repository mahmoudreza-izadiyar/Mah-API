from django.contrib import admin
from .models import Note
# Register your models here.

class NoteAdmin(admin.ModelAdmin):
    fields = ('title', 'context')

admin.site.register(Note)