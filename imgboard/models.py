from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

class Thread(models.Model):
	date_created = models.DateTimeField(default=timezone.now)
	thread_name = models.CharField(max_length=50)
	bump_thread = models.IntegerField(default=0)

class Post(models.Model):
	thread = models.ForeignKey(Thread)
	date_published = models.DateTimeField('date published')
	post_text = models.CharField(max_length=300)
	pic = models.ImageField(upload_to='pics', blank=True)
