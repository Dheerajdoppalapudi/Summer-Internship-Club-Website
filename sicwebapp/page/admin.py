from django.contrib import admin
from .models import Post, Member, Suggestions

# Register your models here.
admin.site.register(Post)
admin.site.register(Member)
admin.site.register(Suggestions)