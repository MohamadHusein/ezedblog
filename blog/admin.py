from django.contrib import admin
from . import models


class FilterByTitle(admin.SimpleListFilter):
    title = 'کلمه های پر تکرار'
    parameter_name = 'title'

    def lookups(self, request, model_admin):
        return (
            ('java' , 'جاوا'),
            ('Cyber security' , 'امنیت سایبری'),
        )

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(title__iexact=self.value())


class CommentInLine(admin.TabularInline):
    model = models.Comment




@admin.register(models.Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'body' , 'show_image')
    search_fields = ('title', 'body')
    list_filter = ('title', FilterByTitle)
    inlines = (CommentInLine,)








admin.site.register(models.Category)
admin.site.register(models.Comment)
admin.site.register(models.Massage)
admin.site.register(models.Like)

