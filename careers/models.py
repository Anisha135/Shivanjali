from django.db import models
from django.core.validators import MinLengthValidator,MaxLengthValidator
from django.core.validators import MinValueValidator,MaxValueValidator

class Internship(models.Model):
	name = models.CharField(max_length=100)
	email = models.EmailField()
	phone_number = models.PositiveIntegerField(validators=[MaxValueValidator(9999999999),MinValueValidator(1000000000)])
	age = models.PositiveIntegerField(validators=[MaxValueValidator(150),MinValueValidator(1)])
	resume = models.FileField(upload_to='resumes/internship_resume/')
	role = models.CharField(max_length=100)
	experience = models.CharField(max_length=100)
	motivation = models.TextField(max_length=100)

class Volunteer(models.Model):
	name = models.CharField(max_length=100)
	email = models.EmailField()
	phone_number = models.PositiveIntegerField(validators=[MaxValueValidator(9999999999),MinValueValidator(1000000000)])
	age = models.PositiveIntegerField(validators=[MaxValueValidator(150),MinValueValidator(1)])
	resume = models.FileField(upload_to='resumes/volunteer_resume/')
	role = models.CharField(max_length=100)
	experience = models.CharField(max_length=100)
	motivation = models.TextField(max_length=100)

