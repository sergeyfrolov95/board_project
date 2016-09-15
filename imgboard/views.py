from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return HttpResponse("There will be list of threads")