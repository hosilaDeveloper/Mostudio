from django.contrib import admin
from .models import Home, Gallery, About, Pricing, Contact, Category

# Register your models here.


class HomeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category')
    list_display_links = ('id', 'title', 'category')


admin.site.register(Home, HomeAdmin)
admin.site.register(Gallery)
admin.site.register(About)
admin.site.register(Pricing)
admin.site.register(Contact)
admin.site.register(Category)

