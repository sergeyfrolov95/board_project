from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.base import View
from django.utils import timezone

from .models import Thread, Post
from .forms import PostForm

def index(request):
	thread_list = Thread.objects.all()
	context = {'thread_list': thread_list}
	return render(request, 'index.html', context)

def thread(request, thread_id):
	thread = get_object_or_404(Thread, pk=thread_id)
	context = {
		'thread': thread,
	}
	return render(request, 'thread.html', context)

class ThreadView(View):
	post_form = PostForm
	initial = {'key': 'value'}

	def get(self, request, thread_id, **keargs):
		thread = get_object_or_404(Thread, pk=thread_id)
		form = self.post_form(initial=self.initial)
		context = {
			'thread': thread,
			'form': form,
		}
		return render(request, 'thread.html', context)

	def post(self, request, **kwargs):
		form = self.post_form(request.POST, request.FILES)
		if form.is_valid():
			p = Post(post_text=form.cleaned_data['post_text'],
				date_published=timezone.now(), thread_id=kwargs['thread_id'])
			p.pic = request.FILES.get('picture', '')
			p.save()
			return HttpResponseRedirect('')
		else:
			return HttpResponseRedirect('')
