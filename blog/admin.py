from django.contrib import admin
from .models import Post, Project, Connect

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_on')
    search_fields = ['title', 'content']

# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Connect)

