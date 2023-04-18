from django.urls import include, path, re_path

from rest_framework import routers

from api.v1.views import (
    CommentViewSet,
    FollowViewSet,
    GroupViewSet,
    PostViewSet
)

app_name = 'api'

router = routers.DefaultRouter()
router.register(
    r'posts',
    PostViewSet,
    basename='post'
)

router.register(
    r'groups',
    GroupViewSet,
    basename='group'
)

router.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comment'
)

router.register(
    r'follow',
    FollowViewSet,
    basename='follow'
)

urlpatterns = [
    re_path('', include(router.urls)),
    path('', include('djoser.urls')),
    path('', include('djoser.urls.jwt')),
]
