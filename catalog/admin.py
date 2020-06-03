from django.contrib import admin

# Register your models here.

from .models import User, Profile

# register user model
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass

# register profile model
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'national_id', 'age', 'gender')
