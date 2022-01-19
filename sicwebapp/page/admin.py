from django.contrib import admin
from .models import Post, Member, Suggestions, Certifications, Scolarships, Hackathons, Fellowships, Competetive

# Register your models here.
admin.site.register(Post)
admin.site.register(Member)
admin.site.register(Suggestions)
admin.site.register(Certifications)
admin.site.register(Scolarships)
admin.site.register(Hackathons)
admin.site.register(Fellowships)
admin.site.register(Competetive)
