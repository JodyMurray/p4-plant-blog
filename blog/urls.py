from . import views
from django.urls import path


urlpatterns = [
    path("", views.PostList.as_view(), name="home"),
    path('featured/', views.FeaturedView.as_view(), name='featured'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]
