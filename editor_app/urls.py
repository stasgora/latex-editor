from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('home/', views.home, name='home'),
	path('new/', views.new, name='new'),
	path('edit/<int:formula_id>/', views.editor, name='editor'),
	path('save/', views.save, name='save'),
]
