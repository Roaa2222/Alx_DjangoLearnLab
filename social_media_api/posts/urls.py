from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)
urlpatterns = [
    path('feed/', FeedView.as_view(), name='feed'),
]
urlpatterns = router.urls
