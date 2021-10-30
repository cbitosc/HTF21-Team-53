from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(events)
admin.site.register(clubs)
admin.site.register(registration_details)
admin.site.register(registration)

