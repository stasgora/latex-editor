import django
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render, redirect

from editor_app.models import Formula


def index(request):
	return render(request, 'index.html')


@login_required
def home(request):
	is_user_moderator = request.user.groups.filter(name='Moderatorzy').exists() or request.user.is_superuser
	formulas = Formula.objects.filter(Q(owner=request.user))
	other_formulas = Formula.objects.filter(~Q(owner=request.user)) if is_user_moderator else []
	return render(request, 'home.html', {'formulas': formulas, 'other_formulas': other_formulas})


@login_required
def editor(request, formula_id):
	try:
		formula = Formula.objects.get(id=formula_id, owner=request.user)
	except Formula.DoesNotExist:
		messages.add_message(request, messages.ERROR, 'Nie znaleziono formuły')
		return redirect('home')
	return render(request, 'editor.html', {'formula': formula})


@login_required
def new(request):
	return render(request, 'editor.html', {'formula': {'title': '', 'text': ''}})


@login_required
def save(request):
	id = request.POST['id']
	if id != '':
		formula, _ = Formula.objects.get_or_create(id=id)
		formula.text = request.POST['text']
		formula.title = request.POST['title']
		formula.save()
	else:
		Formula.objects.create(text=request.POST['text'], title=request.POST['title'], owner=request.user)
	return redirect('home')


def remove(request, formula_id):
	Formula.objects.get(id=formula_id).delete()
	return redirect('home')


def auth(request):
	redirect_path = request.POST['next'] if ('next' in request.POST and request.POST['next']) else 'home'

	if not request.POST['username'] or not request.POST['password']:
		messages.add_message(request, messages.ERROR, 'Wpisz dane logowania')
	elif 'singIn' in request.POST:
		if not User.objects.filter(username=request.POST['username']).exists():
			User.objects.create_user(request.POST['username'], password=request.POST['password'])
			user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
			login(request, user)
			return redirect(redirect_path)
		else:
			messages.add_message(request, messages.ERROR, 'Nazwa użytkownika zajęta')
	elif 'logIn' in request.POST:
		user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
		if user is not None:
			login(request, user)
			return redirect(redirect_path)
		else:
			messages.add_message(request, messages.ERROR, 'Niepoprawne dane logowania')
	return redirect('/')


@login_required
def logout(request):
	django.contrib.auth.logout(request)
	return redirect('/')
