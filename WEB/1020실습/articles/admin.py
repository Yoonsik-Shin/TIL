from django.contrib import admin
from .models import Article, Comment

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'user']

class CommentAdmin(admin.ModelAdmin):
    list_display = ['content', 'article', 'user']

admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)