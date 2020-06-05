from django.db import models

# Create your models here.
class User(models.Model):

    #fields
    national_id = models.BigIntegerField(help_text='Enter National ID', primary_key=True)
    password = models.CharField(max_length=30, help_text='Enter password')

    def __str__(self):
        return self.national_id

class Idcard(models.Model):

    religion_options = (
        ('muslim', 'مسلم'),
        ('Christian', 'مسيحي'),
        ('Godless', 'بلا ديانة'),
    )

    gender_type = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    social_status_options = (
        ('married', 'متزوج'),
        ('Widowed', 'أرمل'),
        ('divorced','مطلق'),
        ('single', 'أعزب'),
    )

  
    national_id = models.BigIntegerField(default= 123456789, help_text='Enter National ID', primary_key=True)
    first_name = models.CharField(max_length=15, help_text='Enter First Name')
    father_name = models.CharField(max_length=100, help_text='Enter Father Complete Name')
    mother_name = models.CharField(max_length=100, help_text='Enter Mother Name')
    religion = models.CharField(max_length=30, choices=religion_options)
    gender = models.CharField(max_length=1, choices=gender_type)
    social_status = models.CharField(max_length=50, choices=social_status_options)
    governorate = models.CharField(max_length=15, default='mansoura')
    department = models.CharField(max_length=30, default='45')
    village = models.CharField(max_length=30, default='45')
    building_number = models.IntegerField(default=1)
    street = models.CharField(max_length=30, default='45')
    floor_number = models.IntegerField(default=1)
    aprtment = models.IntegerField(default=1) #الشقة
    phone_number = models.IntegerField(default=10022334455, help_text='Enter Phone Number')
    residential_pool = models.CharField(max_length=30, default='45')
    #photograph = models.ImageField(upload_to='media')

    def __str__(self):
        return self.first_name

class Driving_license(models.Model):

    traffic_police_area = models.CharField(max_length=30)
    quadruple_name = models.CharField(max_length=100)
    national_id = models.BigIntegerField(help_text='Enter National ID', primary_key=True)
    phone_number = models.IntegerField(help_text='Enter Phone Number')
    address = models.CharField(max_length=100, help_text='Enter address')
    date_of_birth = models.DateField(help_text='Enter Date of Birth')

    def __str__(self):
        return self.national_id



class Profile(models.Model):

    gender_type = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    #driving license options 
    yes_or_no = (
        ('Y', 'Yes'),
        ('N', 'No'),
    )

    #social status options
    social_status_options = (
        ('married', 'متزوج'),
        ('Widowed', 'أرمل'),
        ('divorced','مطلق'),
        ('single', 'أعزب'),
    )

    name = models.CharField(max_length=70, help_text='Enter profile name')
    national_id = models.BigIntegerField(help_text='Enter National ID', primary_key=True)
    age = models.PositiveSmallIntegerField(help_text='Enter age')
    gender = models.CharField(max_length=1, choices=gender_type)
    address = models.CharField(max_length=100)
    academic_status = models.CharField(max_length=50)
    # محتاجة نضيف هنا خيارات بالحالة الاجتماعيه في البطاقة
    social_status = models.CharField(max_length=50, choices=social_status_options)
    job = models.CharField(max_length=50)
    driving_license = models.CharField(max_length=1, choices=yes_or_no, help_text='add if thier driving license or not')

    def __str__(self):
        return self.name



""" class birthregisteration(models.Model):
class premiumservice(models.Model):
class nationalidregesteration(models.Model):
class drivinglicenseregisteration(models.Model):
class payment(models.Model):  """