from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import RegisteredAlumni, Alumni

class AlumniAdmin(admin.ModelAdmin):
    list_display = ('id', 'last_name', 'first_name', 'school_id', 'email', 'year_graduated')
    search_fields = ('last_name', 'first_name', 'email')  
    ordering = ('last_name', 'first_name')  

admin.site.register(Alumni, AlumniAdmin)

class RegisteredAlumniAdmin(UserAdmin):

    list_display = ('email', 'first_name', 'last_name', 'school_id', 'is_active', 'is_admin')
    
    search_fields = ('email', 'first_name', 'last_name')

    ordering = ('email',)

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'school_id')}),
        ('Permissions', {'fields': ('is_active', 'is_admin')}),
    )
    
    readonly_fields = ('id',)

    list_filter = ('is_active', 'is_admin')

    filter_horizontal = ()
    
    add_fieldsets = (
        (None, {'fields': ('email', 'password1', 'password2')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'school_id')}),
        ('Permissions', {'fields': ('is_active', 'is_admin')}),
    )

admin.site.register(RegisteredAlumni, RegisteredAlumniAdmin)
