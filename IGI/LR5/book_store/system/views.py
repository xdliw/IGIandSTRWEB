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
def buying_product(request, product_id):
	return HttpResponse("здесь будет переход к оплате через внешний сервис")


@login_required
def orders(request):
	if request.user.is_staff:
		orders = get_list_or_404(Order)
		context = {'orders': orders, 'title': 'Заказы клиентов'}
	else:
		orders = get_list_or_404(Order, client__pk=request.user.client.pk)
		context = {'orders': orders, 'title': 'Ваши заказы'}
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










