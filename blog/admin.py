from django.contrib import admin

# Register your models here.
from blog.models import Article, Page, Comment
# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date')
    ordering = ('date', )


class PageAdmin(admin.ModelAdmin):
    list_display = ('title',)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'authorEmail', 'date')


admin.site.register(Article, ArticleAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(Comment, CommentAdmin)
