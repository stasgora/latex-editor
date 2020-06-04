from django.shortcuts import render, get_object_or_404, redirect

from editor_app.models import Formula


def index(request):
	return render(request, 'home.html')


def editor(request, formula_id):
	formula = get_object_or_404(Formula, id=formula_id)
	return render(request, 'editor.html', {'formula': formula})


def save(request, formula_id):
	formula, _ = Formula.objects.get_or_create(id=formula_id)
	formula.text = request.POST['text']
	formula.save()
	return redirect('/')
