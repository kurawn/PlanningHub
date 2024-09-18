from django.contrib import admin

from apps.planning_permission.models import Detail


@admin.register(Detail)
class DetailAdmin(admin.ModelAdmin):
    list_display = ('id', 'restriction', 'description')
    search_fields = ('description',)
    list_filter = ('restriction',)
    filter_horizontal = ('planning_codes',)
