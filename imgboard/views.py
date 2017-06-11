from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.base import View
from django.utils import timezone

from .models import Thread, Post
from .forms import PostForm, ThreadForm

class IndexView(View):
	thread_form = ThreadForm
	initial = {'key': 'value'}

	def get(self, request, **kwargs):
		form = self.thread_form(initial=self.initial)
		thread_list = Thread.objects.all()
		context = {'thread_list': thread_list,
					'form': form,
		}
		return render(request, 'index.html', context)

	def post(self, request):
		form = self.thread_form(request.POST)
		if form.is_valid():
			t = Thread(thread_name=form.cleaned_data['thread_name'])
			t.save()
			return HttpResponseRedirect('/board')
		else:
			return HttpResponseRedirect('/board')



class ThreadView(View):
	post_form = PostForm
	initial = {'key': 'value'}

	def get(self, request, thread_id, **kwargs):
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
			return HttpResponseRedirect('/board/thread' + kwargs['thread_id'])
		else:
			return HttpResponseRedirect('/board/thread' + kwargs['thread_id'])
