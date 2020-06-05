from django.contrib import admin

# Register your models here.

from .models import User, Idcard, Driving_license, Profile

# register user model
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('national_id', 'password')

@admin.register(Idcard)
class IdcardAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'father_name')

@admin.register(Driving_license)
class Driving_licenseAdmin(admin.ModelAdmin):
    list_display = ('national_id', 'phone_number')

# register profile model
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'national_id', 'age', 'gender')