from django.contrib import admin
from listings.models import band,Listing


class bandAdmin(admin.ModelAdmin):
    list_display=('name','year_formed','genre')
class listingAdmin(admin.ModelAdmin):
    list_display=('title','description','type','band')

admin.site.register(band,bandAdmin)
admin.site.register(Listing,listingAdmin)

# Register your models here.
