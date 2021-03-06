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
		thread_list = Thread.objects.all().order_by('-bump_thread', '-id')
		context = {'thread_list': thread_list,
					'form': form,
		}
		return render(request, 'index.html', context)


	def post(self, request):
		form = self.thread_form(request.POST)
		if form.is_valid():
			t = Thread(thread_name=form.cleaned_data['thread_name'])
			t.save()
			past = timezone.datetime.today() - timezone.timedelta(days=14)
			Thread.objects.filter(date_created__lte=past).delete()
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
		valid_bump_variants = ('bump', 'Bump', 'Bump', 'bump!')
		form = self.post_form(request.POST, request.FILES)
		if form.is_valid():
			p = Post(post_text=form.cleaned_data['post_text'],
				date_published=timezone.now(), thread_id=kwargs['thread_id'])
			p.pic = request.FILES.get('picture', '')
			p.save()
			thread = get_object_or_404(Thread, pk=kwargs['thread_id'])
			if p.post_text in valid_bump_variants and Post.objects.filter(thread=kwargs['thread_id']).count() < 100:
				thread.bump_thread += 1
				thread.save()
		return HttpResponseRedirect('/board/thread' + kwargs['thread_id'])
