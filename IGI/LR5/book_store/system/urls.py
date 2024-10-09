from django.urls import path
from . import views

urlpatterns = [
	path('catalog/', views.catalog, name='catalog'),
	path('product/<int:product_id>/', views.product, name='product'),
	path('buying_product/<int:product_id>/', views.buying_product, name='buying_product'), #undone
	path('orders/', views.orders, name='orders'),
	path('client_info/<int:client_id>', views.client_info, name='client_info'),
	path('personal_cabinet/', views.personal_cabinet, name='personal_cabinet'),
]