from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Thread, Post

def index(request):
	thread_list = Thread.objects.all()
	context = {'thread_list': thread_list}
	return render(request, 'imgboard/index.html', context)

def thread(request, thread_id):
	thread = get_object_or_404(Thread, pk=thread_id)
	context = {
		'thread': thread,
	}
	return render(request, 'imgboard/thread.html', context)
