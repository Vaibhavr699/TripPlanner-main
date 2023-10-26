from django.contrib import admin
from .models import Spot, Gallery, Trip, Profile

admin.site.register(Trip)
admin.site.register(Profile)
admin.site.register(Spot)
admin.site.register(Gallery)
