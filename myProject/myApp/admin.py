from django.contrib import admin
from django.contrib.auth.models import User

from .models import Alumni

class AlumniAdmin(admin.ModelAdmin):
    list_display='id', 'lastname', 'firstname', 'middlename', 'gender', 'email', 'password', 'year_graduated'
    
admin.site.register(Alumni, AlumniAdmin)


from django.contrib.auth.admin import UserAdmin
from .models import RegisteredAlumni

class RegisteredAlumniAdmin(UserAdmin):
    list_display = ('email', 'username', 'is_active', 'is_admin')
    search_fields = ('email', 'username')
    readonly_fields = ('id',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(RegisteredAlumni, RegisteredAlumniAdmin)
