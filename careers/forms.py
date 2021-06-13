from django import forms
from django.core.validators import MinLengthValidator,MaxLengthValidator
from django.core.validators import MinValueValidator,MaxValueValidator
from .models import Internship,Volunteer

class Internshipform(forms.ModelForm):
	class Meta:
		model = Internship
		fields = ["name","email","phone_number","age","resume","role","experience","motivation"]

class Volunteerform(forms.ModelForm):
	class Meta:
		model = Volunteer
		fields = ["name","email","phone_number","age","resume","role","experience","motivation"]


	
