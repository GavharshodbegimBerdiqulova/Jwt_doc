from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import BookViewSet, RegisterView

router = DefaultRouter()
router.register('books', BookViewSet, basename='book')

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('', include(router.urls)),
]
