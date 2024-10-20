from django.urls import path
from . import views

urlpatterns = [
	path('about/', views.about, name='about'),
	path('news/', views.news, name='news'),
	path('article/<int:article_id>/', views.article, name='article'),
	path('contacts/', views.contacts, name='contacts'),
	path('coupons/', views.coupons, name='coupons'),
	path('faq/', views.faq, name='faq'),
	path('', views.index, name='index'),
	path('privacy/', views.privacy, name='privacy'),
	path('reviews/', views.reviews, name='reviews'),
	path('vacancies/', views.vacancies, name='vacancies'),
	path('no-access/', views.no_access, name='no-access'),
	path('add-review/', views.add_review, name='add-review'),
]