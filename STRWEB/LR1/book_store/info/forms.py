from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
	class Meta:
		model = Review
		fields = ['body', 'grade']
		labels = {
			'body': 'Сообщение',
			'grade': 'Оценка',
		}
