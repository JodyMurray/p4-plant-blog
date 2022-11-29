from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("blog.urls"), name="blog.urls"),
    url(r'^newsletter/', include("newsletter.urls"), name="newsletter.urls"),
    path('summernote/', include('django_summernote.urls')),
    path('accounts/', include("allauth.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

