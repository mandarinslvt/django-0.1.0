from django.contrib import admin
from .models import Category, Dish, Post 

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'is_available', 'created_at')
    list_filter = ('is_available', 'category')
    search_fields = ('name', 'description')
    list_editable = ('price', 'is_available')
    prepopulated_fields = {'slug': ('name',)}
    list_select_related = ('category',)
    date_hierarchy = 'created_at'
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Основное', {
            'fields': ('category', 'name', 'slug', 'description')
        }),
        ('Цена и наличие', {
            'fields': ('price', 'is_available')
        }),
        ('Медиа', {
            'fields': ('image',)
        }),
        ('Служебное', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )