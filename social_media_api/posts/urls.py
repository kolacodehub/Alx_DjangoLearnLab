from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, UserFeedView, LikePostView, UnlikePostView

router = DefaultRouter()

# The first argument is the URL prefix (e.g., 'posts' means the URL will be /posts/)
router.register(r"posts", PostViewSet, basename="post")
router.register(r"comments", CommentViewSet, basename="comment")

urlpatterns = [
    # Putting the feed URL FIRST so the router doesn't accidentally swallow it
    path('feed/', UserFeedView.as_view(), name='user_feed'),
    path("", include(router.urls)),
    
    path('posts/<int:pk>/like/', LikePostView.as_view(), name='like_post'),
    path('posts/<int:pk>/unlike/', UnlikePostView.as_view(), name='unlike_post'),
]
