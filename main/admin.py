from django.contrib import admin

from .models import Category, Comment, Notice, Place


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'address', 'created', 'updated']
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ['created', 'updated', 'category']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'places', 'text']


@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    pass
