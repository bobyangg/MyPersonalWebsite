from django.contrib import admin
from . import models

# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'technology', 'image', 'link')
    list_filter = ('title', )
    ordering = ('title', )
    search_field = ('title', )

admin.site.register(models.Project, ProjectAdmin)

class WorkAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'description2', 'image', 'link')
    list_filter = ('title', )
    ordering = ('title', )
    search_field = ('title', )

admin.site.register(models.Work, WorkAdmin)
