from django.db import models


class Formula(models.Model):
	title = models.TextField(default='', verbose_name='Tytuł formuły')
	text = models.TextField(verbose_name='Formuła matematyczna w języku Latex')

	def __str__(self):
		return self.title + ': ' + self.text
