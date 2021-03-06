from django.contrib import admin

from .models import Thread, Post

class PostInLine(admin.TabularInline):
    model = Post
    extra = 3

class ThreadAdmin(admin.ModelAdmin):
    inlines = [PostInLine]

admin.site.register(Thread, ThreadAdmin)
admin.site.register(Post)

# auth for admin
# 127.0.0.1:8000/admin
