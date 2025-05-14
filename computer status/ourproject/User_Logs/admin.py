from django.contrib import admin
from django.utils.html import format_html
from .models import UserLog

@admin.register(UserLog)
class UserLogAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'computer_name', 'action', 'status', 'formatted_timestamp', 'edit_link', 'delete_link')  # Add status
    search_fields = ('user__username', 'action', 'computer_name', 'status')  # Add status to search
    list_filter = ('timestamp', 'action', 'status')  # Add status to filters
    ordering = ('-timestamp',)  # Order by timestamp descending
    list_per_page = 10  # Limit the number of items per page

    def formatted_timestamp(self, obj):
        """Format the timestamp for better readability."""
        return obj.timestamp.strftime('%Y-%m-%d %H:%M:%S')  # Format as 'YYYY-MM-DD HH:MM:SS'
    formatted_timestamp.short_description = 'Time and Date'

    def edit_link(self, obj):
        """Provide a link to edit the object."""
        return format_html('<a href="{}">Edit</a>', f'/admin/User_Logs/userlog/{obj.id}/change/')
    edit_link.short_description = 'Edit'

    def delete_link(self, obj):
        """Provide a link to delete the object."""
        return format_html('<a href="{}" style="color: red;">Delete</a>', f'/admin/User_Logs/userlog/{obj.id}/delete/')
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
