from django.shortcuts import redirect, render, get_object_or_404, get_list_or_404
from django.http import HttpResponseNotFound
from django.contrib.auth.decorators import login_required

from system.models import Coupon
from users.models import Client, Employee
from .models import *
from .forms import *


def about(request):
	company = Company.objects.first()
	return render(request, 'info/about.html', context={'company': company})


def news(request):
	news = Article.objects.all()
	return render(request, 'info/news.html', {'news':news})


def article(request, article_id):
	article = get_object_or_404(Article, pk=article_id)
	return render(request, 'info/article.html', {'article':article})


def contacts(request):
	employees = Employee.objects.all()
	context = {'title': 'Контакты', 'employees': employees}
	return render(request, 'info/contacts.html', context)


def coupons(request):
	coupons = Coupon.objects.all()
	return render(request, 'info/coupons.html', {'title': 'Купоны', 'coupons': coupons})


def faq(request):
	faq = Faq.objects.all()
	return render(request, 'info/faq.html', context={'faq': faq})


def index(request):
	article = Article.objects.latest('last_modification_date')
	context = {'title': 'Главная страница', 'article': article}
	return render(request, 'info/index.html', context)


def privacy(request):
	return render(request, 'info/privacy.html', {'title': 'Политика конфиденциальности'})


def reviews(request):
	reviews = Review.objects.all()
	context = {'title': 'Отзывы', 'reviews': reviews}
	return render(request, 'info/reviews.html', context)


def vacancies(request):
	vacancy_list = Vacancy.objects.all()
	context = {'vacancy_list': vacancy_list}
	return render(request, 'info/vacancies.html', context)


def page_not_found(request, exception=None):
	return HttpResponseNotFound("<h1>Страница не найдена</h1>")


def no_access(request):
	return render(request, 'no_access.html')


@login_required
def add_review(request):
	if request.user.is_staff:
		return redirect('reviews')
	
	if request.method == 'POST':
		form = ReviewForm(request.POST)
		if form.is_valid():
			review = form.save(commit=False)
			review.client = Client.objects.get(user=request.user)
			review.save()
			return redirect('reviews')
	else:
		form = ReviewForm()
	return render(request, 'info/add_review.html', {'form': form})