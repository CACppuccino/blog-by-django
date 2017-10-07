from django.shortcuts import render, redirect
from django.views import View

def index_page(request):
	return render('index.html')
