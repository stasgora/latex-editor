from django.db import models


class Formula(models.Model):
	text = models.TextField(verbose_name='Mathematical formula written in plain Latex')

	def __str__(self):
		return self.text
