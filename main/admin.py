from django.contrib import admin
from django.contrib.auth.models import User, Group

from .models import *

admin.site.unregister(User)
admin.site.unregister(Group)


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'created_at')
    search_fields = ('name', 'phone_number')
    date_hierarchy = 'created_at'


admin.site.register(Contact, ContactAdmin)
