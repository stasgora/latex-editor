from django.shortcuts import render

from editor_app.models import Formula


def index(request):
	formula = Formula.objects.first()
	return render(request, 'index.html', {'formula': formula})
