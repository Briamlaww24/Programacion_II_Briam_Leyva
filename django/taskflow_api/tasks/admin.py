from django.contrib import admin
from .models import Project
from .models import library
from .models import Category
# Register your models here.

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at")
    search_fields = ("name",)

@admin.register(Category)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)

@admin.register(library)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("book_name", "created_at")
    search_fields = ("book_name",)
