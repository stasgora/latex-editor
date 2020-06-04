from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('edit/<int:formula_id>/', views.editor, name='editor'),
	path('save/<int:formula_id>/', views.save, name='save'),
]