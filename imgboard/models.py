from __future__ import unicode_literals

from django.db import models

class Thread(models.Model):
	thread_name = models.CharField(max_length=50)

class Post(models.Model):
	thread = models.ForeignKey(Thread)
	date_published = models.DateTimeField('date published')
	post_text = models.CharField(max_length=300)
