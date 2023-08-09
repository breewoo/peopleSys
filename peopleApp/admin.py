from django.contrib import admin
from . import models



class PeopleAdmin(admin.ModelAdmin):
    list_display = ['name', 'gender', 'age']
    search_fields = ['name']
    list_per_page = 25


admin.site.register(models.People, PeopleAdmin)