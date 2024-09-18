from django.contrib import admin

from apps.planning_permission.models import PlanningPermissionCode


@admin.register(PlanningPermissionCode)
class PlanningPermissionCodeAdmin(admin.ModelAdmin):
    list_display = ('id', 'code', 'category', 'requires_permission')
    list_filter = ('category', 'requires_permission')
    search_fields = ('code', 'description')
