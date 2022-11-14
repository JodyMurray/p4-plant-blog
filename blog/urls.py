from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
from django.urls import path
from . import views
from .views import AddPostView, UserSettings, UserProfile
from .models import Profile


urlpatterns = [
    path("", views.PostList.as_view(), name="home"),
    path('featured/', views.FeaturedView.as_view(), name='featured'),
    path('profile/', login_required(UserProfile.as_view()), name='profile'),
    path('edit_profile/', login_required(UserSettings.as_view()), name='edit_profile'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>/', views.PostLike.as_view(), name='post_like'),
]
