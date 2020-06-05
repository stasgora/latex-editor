import django
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect

from editor_app.models import Formula


def index(request):
	return render(request, 'index.html')


def home(request):
	if not request.user.is_authenticated:
		return redirect('/')
	formulas = Formula.objects.filter(owner=request.user)
	return render(request, 'home.html', {'formulas': formulas})


def editor(request, formula_id):
	if not request.user.is_authenticated:
		return redirect('/')
	formula = get_object_or_404(Formula, id=formula_id)
	return render(request, 'editor.html', {'formula': formula})


def new(request):
	if not request.user.is_authenticated:
		return redirect('/')
	return render(request, 'editor.html', {'formula': {'title': '', 'text': ''}})


def save(request):
	if not request.user.is_authenticated:
		return redirect('/')
	id = request.POST['id']
	if id != '':
		formula, _ = Formula.objects.get_or_create(id=id)
		formula.text = request.POST['text']
		formula.title = request.POST['title']
		formula.save()
	else:
		Formula.objects.create(text=request.POST['text'], title=request.POST['title'], owner=request.user)
	return redirect('home')


def auth(request):
	if 'singIn' in request.POST:
		if not User.objects.filter(username=request.POST['username']).exists():
			User.objects.create_user(request.POST['username'], password=request.POST['password'])
			return redirect('home')
		else:
			messages.add_message(request, messages.ERROR, 'Nazwa użytkownika zajęta')
	elif 'logIn' in request.POST:
		user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
		if user is not None:
			login(request, user)
			return redirect('home')
		else:
			messages.add_message(request, messages.ERROR, 'Niepoprawne dane logowania')
	return redirect('/')


def logout(request):
	if not request.user.is_authenticated:
		return redirect('/')
	django.contrib.auth.logout(request)
	return redirect('/')
