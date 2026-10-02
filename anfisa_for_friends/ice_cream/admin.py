from django.contrib import admin

from .models import Category, IceCream, Topping, Wrapper


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'output_order', 'is_published')
    list_editable = ('is_published',)
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Topping)
class ToppingAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'is_published')
    list_editable = ('is_published',)
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Wrapper)
class WrapperAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_published')
    list_editable = ('is_published',)


@admin.register(IceCream)
class IceCreamAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'category', 'wrapper', 'is_on_main', 'is_published'
    )
    list_editable = ('is_on_main', 'is_published')
    list_filter = ('category', 'is_published')
    search_fields = ('title', 'description')
    filter_horizontal = ('toppings',)
