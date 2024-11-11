from django.db import models

# Create your models here.
from django.db import models

# Student Model
class Student(models.Model):
    first_name = models.CharField(max_length=100)  # Field para sa first name
    last_name = models.CharField(max_length=100)  # Field para sa last name
    email = models.EmailField()  # Field para sa email address
    date_of_birth = models.DateField()  # Field para sa birthday
    enrollment_date = models.DateTimeField(auto_now_add=True)  # Field para sa date kung kailan na-enroll

    def __str__(self):
        return f"{self.first_name} {self.last_name}"  # Tama para sa Student

# Teacher Model (Hiwalay sa Student model)
class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.subject}"  # Tama para sa Teacher

