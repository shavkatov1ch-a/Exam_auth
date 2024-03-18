from django.contrib import admin
from .models import City, Category, Tag

class CityAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    list_filter = ('title','created_at', 'updated_at')


admin.site.register(City, CityAdmin)
admin.site.register(Category)
admin.site.register(Tag)