from django.http import Http404
from django.shortcuts import render

from editor_app.models import Formula


def index(request):
	formula = Formula.objects.first()
	return render(request, 'home.html')


def editor(request, formula_id):
	try:
		formula = Formula.objects.get(id=formula_id)
	except Formula.DoesNotExist:
		raise Http404('Formuła nie istnieje')
	return render(request, 'editor.html', {'formula': formula})
