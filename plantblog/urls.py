from django.contrib import admin
from django.urls import path, include
from .views import profile



urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("blog.urls"), name="blog.urls"),
    path('summernote/', include('django_summernote.urls')),
    path('accounts/', include("allauth.urls")),
    path('profile/', profile, name='users-profile'),
]

