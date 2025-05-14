# from django.contrib import admin
# from django.utils.html import format_html
# from .models import UserRoles

# @admin.register(UserRoles)
# class UserRolesAdmin(admin.ModelAdmin):
#     list_display = ('id', 'username', 'password', 'edit_link', 'delete_link')  # Add Edit and Delete links
#     search_fields = ('username',)  # Add a search bar for username
#     ordering = ('username',)  # Order by username
#     list_filter = ('role',)  # Add a filter for role
#     list_per_page = 10  # Limit the number of items per page

#     def edit_link(self, obj):
#         """Provide a link to edit the object."""
#         return format_html('<a href="{}">Edit</a>', f'/admin/User_Roles/userroles/{obj.id}/change/')
#     edit_link.short_description = 'Edit'

#     def delete_link(self, obj):
#         """Provide a link to delete the object."""
#         return format_html('<a href="{}" style="color: red;">Delete</a>', f'/admin/User_Roles/userroles/{obj.id}/delete/')
#     delete_link.short_description = 'Delete'
