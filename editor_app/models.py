from django.contrib.auth.models import User
from django.db import models


class Formula(models.Model):
	owner = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.TextField(default='', verbose_name='Tytuł wyrażenia')
	text = models.TextField(verbose_name='Wyrażenie matematyczna w języku LaTeX')

	@classmethod
	def create(cls, title, text):
		return cls(title=title, text=text)

	def __str__(self):
		return self.title + ': ' + self.text
