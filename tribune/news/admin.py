from django.contrib import admin

from .models import Article, tags

TEXT = 'Section description'


class ArticleAdmin(admin.ModelAdmin):
    filter_horizontal = ('tags',)
    fieldsets = (
        ('Section 1', {
            'fields': ('title', 'editor'),
            'description': '%s' % TEXT,
        }),
        ('Section 2', {
            'fields': ('post',)
        })
    )


admin.site.register(Article, ArticleAdmin)
admin.site.register(tags)
