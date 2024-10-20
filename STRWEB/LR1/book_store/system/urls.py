from django.urls import path
from . import views

urlpatterns = [
	path('catalog/', views.catalog, name='catalog'),
	path('product/<int:product_id>/', views.product, name='product'),
	path('orders/', views.orders, name='orders'),
	path('client_info/<int:client_id>', views.client_info, name='client_info'),
	path('personal_cabinet/', views.personal_cabinet, name='personal_cabinet'),
	path('buying_product/<int:product_id>/', views.buying_product, name='buying_product'),
	path('after_buying/<int:product_id>/', views.after_buying, name='after_buying'),
	path('product_out_of_stock/', views.product_out_of_stock, name='product_out_of_stock'),
]