from django.db import models


class Formula(models.Model):
	title = models.TextField(default='', verbose_name='Tytuł formuły')
	text = models.TextField(verbose_name='Formuła matematyczna w języku Latex')

	@classmethod
	def create(cls, title, text):
		return cls(title=title, text=text)

	def __str__(self):
		return self.title + ': ' + self.text
