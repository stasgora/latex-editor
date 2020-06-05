from django.shortcuts import render, get_object_or_404, redirect

from editor_app.models import Formula


def index(request):
	return render(request, 'index.html')


def home(request):
	return render(request, 'home.html')


def editor(request, formula_id):
	formula = get_object_or_404(Formula, id=formula_id)
	return render(request, 'editor.html', {'formula': formula})


def new(request):
	return render(request, 'editor.html', {'formula': {'title': '', 'text': ''}})


def save(request):
	id = request.POST['id']
	if id != '':
		formula, _ = Formula.objects.get_or_create(id=id)
		formula.text = request.POST['text']
		formula.title = request.POST['title']
		formula.save()
	else:
		Formula.objects.create(text=request.POST['text'], title=request.POST['title'])
	return redirect('home')
