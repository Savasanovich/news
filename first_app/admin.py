from django.contrib import admin
from .models import News,Category, About

# Register your models here.


class NewsAdmin(admin.ModelAdmin):
    exclude = ['slug']


class CategoryAdmin(admin.ModelAdmin):
    exclude = ['slug']

class AboutAdmin(admin.ModelAdmin):
    exclude = ['slug']


admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(About, AboutAdmin)

