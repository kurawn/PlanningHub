from django.contrib import admin

from apps.planning_permission.models import Restriction


@admin.register(Restriction)
class RestrictionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
