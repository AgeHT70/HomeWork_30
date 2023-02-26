from django.contrib import admin

from ads.models import Ads, Categories
from users.models import User, Location

admin.site.register(Ads)
admin.site.register(Categories)
admin.site.register(User)
admin.site.register(Location)
