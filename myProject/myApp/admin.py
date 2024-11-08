from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Alumni, RegisteredAlumni

class AlumniAdmin(admin.ModelAdmin):
    list_display = ('id', 'lastname', 'firstname', 'middlename', 'gender', 'email', 'password', 'year_graduated')

admin.site.register(Alumni, AlumniAdmin)

class RegisteredAlumniAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'is_active', 'is_admin')  
    search_fields = ('email',)  # Search by email only since we removed the username
    readonly_fields = ('id',)  # Make ID read-only
    ordering = ('email',)  # Order by email

    # Configure the fieldsets (the layout for the form in the admin)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active', 'is_admin')}),
    )

    # This is typically used for the multiple select widget for User Groups, User Permissions, etc.
    filter_horizontal = ()
    list_filter = ('is_active', 'is_admin')  # Filter by active status or admin status

admin.site.register(RegisteredAlumni, RegisteredAlumniAdmin)
