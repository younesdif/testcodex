"""Admin configuration for the styles app."""

from django.contrib import admin

from .models import Style, SupStyle


class StaffOnlyModelAdmin(admin.ModelAdmin):
    """Allow management only for staff users."""

    def has_view_permission(self, request, obj=None):
        # Allow viewing to authenticated users with change permission behaviour
        # but ensure consistency with staff requirement.
        base_permission = super().has_view_permission(request, obj=obj)
        return request.user.is_staff and base_permission

    def has_module_permission(self, request):
        return request.user.is_staff and super().has_module_permission(request)

    def has_add_permission(self, request):
        return request.user.is_staff and super().has_add_permission(request)

    def has_change_permission(self, request, obj=None):
        return request.user.is_staff and super().has_change_permission(request, obj=obj)

    def has_delete_permission(self, request, obj=None):
        return request.user.is_staff and super().has_delete_permission(request, obj=obj)


@admin.register(SupStyle)
class SupStyleAdmin(StaffOnlyModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Style)
class StyleAdmin(StaffOnlyModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    filter_horizontal = ("supstyles",)
