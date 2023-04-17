from django.urls import include, path, re_path

from rest_framework import routers

from api.views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

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
    re_path('v1/', include(router.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]
