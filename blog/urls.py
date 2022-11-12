from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.urls import path
from .views import UserEditView, AddPostView


urlpatterns = [
    path("", views.PostList.as_view(), name="home"),
    path('featured/', views.FeaturedView.as_view(), name='featured'),
    path('profile/', UserEditView.as_view(), name='profile'),
    path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>/', views.PostLike.as_view(), name='post_like'),
]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL,
#                           document_root=settings.MEDIA_ROOT)
