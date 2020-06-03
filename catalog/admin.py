from django.contrib import admin

# Register your models here.

from .models import User, Idcard

# register user model
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('national_id', 'password')

@admin.register(Idcard)
class IdcardAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'father_name')

""" # register profile model
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'national_id', 'age', 'gender') """