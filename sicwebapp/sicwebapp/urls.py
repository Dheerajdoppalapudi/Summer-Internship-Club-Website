from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from users import views as user_views
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('page.urls')),
    # path('accounts/', include('allauth.urls')),
    path('events/', user_views.events, name='events'),
    path('register/', user_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('accounts/', include('social_django.urls', namespace='social')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = 'Student Internship Club Admin'
admin.site.index_title = "Club Admin"