from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator

from info.models import Vacancy

class Client(models.Model):
	user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
	phone_number = models.CharField(max_length=13, unique=True, validators=[
		RegexValidator(
			regex=r'^\+375(?:29|33|44)\d{7}$',
			message='Номер телефона должен быть в формате: +375(29|33|44)XXXXXXX'
			)])
	date_of_birth = models.DateField()

	def __str__(self):
		return f"{self.user.first_name} {self.user.last_name }"


class Employee(models.Model):
	user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
	phone_number = models.CharField(max_length=25, unique=True, validators=[
		RegexValidator(
			regex=r'^\+375(?:29|33|44)\d{7}$',
			message='Номер телефона должен быть в формате: +375(29|33|44)XXXXXXX'
			)])
	date_of_birth = models.DateField()
	salary = models.FloatField()
	vacancy = models.ForeignKey(Vacancy, on_delete=models.PROTECT, null=True)
	image = models.ImageField(upload_to='images/employees', blank=True)
	
	def __str__(self):
		return f"{self.user.first_name} {self.user.last_name }"


