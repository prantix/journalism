from django.contrib import admin
from .models import Article, Contact

# Register your models here.

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('author', 'category', 'title', 'created', 'updated')
    list_filter = ('author', 'category', 'created')
    prepopulated_fields = {'slug': ('category', 'title',)}

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'message')
    list_filter = ('created', 'first_name', 'last_name')

