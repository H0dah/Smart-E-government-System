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

  
    first_name = models.CharField(max_length=15, help_text='Enter First Name')
    father_name = models.CharField(max_length=100, help_text='Enter Father Complete Name')
    mother_name = models.CharField(max_length=100, help_text='Enter Mother Name')
    religion = models.CharField(max_length=1, choices=religion_options)
    gender = models.CharField(max_length=1, choices=gender_type)
    social_status = models.CharField(max_length=50, choices=social_status_options)
    governorate = models.CharField(max_length=15)
    department = models.CharField(max_length=30)
    village = models.CharField(max_length=30)

    def __str__(self):
        return self.first_name


""" class Profile(models.Model):

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
        return self.name """

""" class services(models.Model):
    service_name = models.CharField
class birthregisteration(models.Model):
class premiumservice(models.Model):
class nationalidregesteration(models.Model):
class drivinglicenseregisteration(models.Model):
class payment(models.Model): """ 