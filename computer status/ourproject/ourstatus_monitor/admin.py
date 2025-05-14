from django.contrib import admin
from django.utils.html import format_html
from .models import Computer  # Import the Computer model

# Customize the admin site headers
admin.site.site_header = "Computer Status Admin Dashboard"
admin.site.site_title = "Computer Status Admin"
admin.site.index_title = "Welcome to the Computer Status Admin Dashboard"

# Register the Computer model with CRUD functionality

class ComputerAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Basic Info', {
            'fields': ('name', 'status'),
        }),
        ('Timestamp', {
            'fields': ('last_updated',),
        }),
    )

    list_display = ('id', 'name', 'status', 'formatted_last_updated', 'edit_link', 'delete_link')  # Fields to display in the list view
    search_fields = ('name',)  # Add a search bar for the 'name' field
    list_filter = ('status', 'last_updated')  # Add filters for 'status' and 'last_updated'
    ordering = ('-last_updated',)  # Order by 'last_updated' descending
    readonly_fields = ('last_updated',)  # Make 'last_updated' read-only
    list_per_page = 10  # Limit the number of items per page
    actions = ['mark_as_available']

    def formatted_last_updated(self, obj):
        """Format the last_updated field for better readability."""
        return obj.last_updated.strftime('%Y-%m-%d %H:%M:%S') if obj.last_updated else 'N/A'
    formatted_last_updated.short_description = 'Last Updated'

    def edit_link(self, obj):
        """Provide a link to edit the object."""
        return format_html('<a href="{}">Edit</a>', f'/admin/ourstatus_monitor/computer/{obj.id}/change/')
    edit_link.short_description = 'Edit'

    def delete_link(self, obj):
        """Provide a link to delete the object."""
        return format_html('<a href="{}" style="color: red;">Delete</a>', f'/admin/ourstatus_monitor/computer/{obj.id}/delete/')
    delete_link.short_description = 'Delete'

    def save_model(self, request, obj, form, change):
        """Customize save behavior if needed."""
        super().save_model(request, obj, form, change)

    def delete_model(self, request, obj):
        """Customize delete behavior if needed."""
        super().delete_model(request, obj)

    def delete_queryset(self, request, queryset):
        """Customize bulk delete behavior."""
        super().delete_queryset(request, queryset)

    def mark_as_available(self, request, queryset):
        """Custom action to mark selected computers as 'Available'."""
        queryset.update(status='Available')
        self.message_user(request, "Selected computers have been marked as 'Available'.")
    mark_as_available.short_description = "Mark selected computers as Available"

# Register the Computer model
admin.site.register(Computer, ComputerAdmin)