from django.contrib import admin

from ads.models import Ads, Categories, Users, Location

admin.site.register(Ads)
admin.site.register(Categories)
admin.site.register(Users)
admin.site.register(Location)
