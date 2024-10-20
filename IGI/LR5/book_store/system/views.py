from django.shortcuts import redirect, render, get_object_or_404, get_list_or_404
from django.http import HttpResponseNotFound, HttpResponse, Http404
from django.contrib.auth.decorators import login_required

from .models import *
from .forms import *

from users.models import Client


def catalog(request):
	products = get_list_or_404(Product)
	
	context = {'products': products, 'title': 'Каталог'}
	return render(request, 'system/catalog.html', context)


def product(request, product_id):
	product = get_object_or_404(Product, id=product_id)
	context = {'product': product, 'title': product.name}
	return render(request, 'system/product.html', context)


@login_required
def orders(request):
	if request.user.is_staff:
		finished_orders = Order.objects.filter(is_finished=True)
		unfinished_orders = Order.objects.filter(is_finished=False)
		context = {'finished_orders': finished_orders, 'unfinished_orders': unfinished_orders, 'title': 'Заказы клиентов'}
	else:
		finished_orders = Order.objects.filter(client__pk=request.user.client.pk, is_finished=True)
		unfinished_orders = Order.objects.filter(client__pk=request.user.client.pk, is_finished=False)
		context = {'finished_orders': finished_orders, 'unfinished_orders': unfinished_orders, 'title': 'Ваши заказы'}
	return render(request,'system/orders.html',context)


@login_required
def client_info(request,client_id):
	if not request.user.is_staff:
		redirect('no-access')
	client = get_object_or_404(Client,id=client_id)
	context = {'client': client, 'title': 'Информация о клиенте'}
	return render(request, 'system/client_info.html', context)


@login_required
def personal_cabinet(request):
	if request.user.is_staff:
		redirect('no-access')
	client = request.user.client
	context = {'client': client, 'title': 'Личный кабинет'}
	return render(request, 'system/personal_cabinet.html', context)


@login_required
def buying_product(request, product_id): #can only buy one at a time. see comment in models.Order
	if request.user.is_staff:
		redirect("no-access")
	product = get_object_or_404(Product, pk = product_id)

	if product.amount <= 0:
		return redirect("product_out_of_stock")
	
	client = request.user.client
	client.order_set.create(product=product)
	product.amount -= 1
	product.save()
	return redirect("after_buying", product_id)


@login_required
def after_buying(request, product_id): # anyone can get here and see the message. I dunno how and won't fix it. Ooh maybe through passing some info through request, maybe via POST. But again, won't fix it.
	product = get_object_or_404(Product, pk=product_id)
	message = f'Ваш заказ на товар "{product.name}" оформлен!'
	context = {'message': message, 'title': 'Успех'} #Успех
	return render(request,"system/message.html", context)


@login_required
def product_out_of_stock(request): # anyone can get here and see the message.
	message = f"К сожалению продукт раскуплен. :("
	context = {'message': message, 'title': 'Неуспех'} #Неуспех
	return render(request, "system/message.html", context)

