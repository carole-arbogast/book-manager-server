from django.urls import include, path
from rest_framework import routers
from . import views
from rest_framework_jwt.views import obtain_jwt_token
from .views import current_user, UserList

router = routers.DefaultRouter()
router.register(r'books', views.BookViewSet)
router.register(r'bookshelves', views.BookshelfViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('token-auth/', obtain_jwt_token),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('current_user/', current_user),
    path('users/', UserList.as_view())
]