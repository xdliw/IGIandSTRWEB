from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone


class ProductType(models.Model):
	name = models.CharField(max_length=50)

	def __str__(self):
		return self.name


class Author(models.Model):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)

	def __str__(self):
		return f"{self.first_name} {self.last_name}"


class Product(models.Model):
	name = models.CharField(max_length=200)
	price = models.FloatField(default = 0, validators=[MinValueValidator(0)])
	product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE)
	authors = models.ManyToManyField(Author)
	amount = models.IntegerField(default = 0, validators=[MinValueValidator(0)])
	amount_sold = models.IntegerField(default = 0, validators=[MinValueValidator(0)])
	image = models.ImageField(upload_to='images/products', blank=True)

	def __str__(self):
		return f"{self.name}"


class Coupon(models.Model):
	is_active = models.BooleanField(default=True)
	code = models.CharField(max_length=12,default='')
	discount = models.FloatField(default=0,validators=[MinValueValidator(0),MaxValueValidator(100)]) #in percent


class Order(models.Model):
	is_finished = models.BooleanField(default = False)
	client = models.ForeignKey('users.Client', on_delete=models.CASCADE)
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	sell_date = models.DateTimeField(default = timezone.now)
	applied_coupon = models.ForeignKey(Coupon, on_delete=models.CASCADE, null=True, blank=True)

