from django.urls import path, include
import rest_framework
from rest_framework import routers


from . import views

router = routers.DefaultRouter()
router.register(r'books', views.BookViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('Books/<int:pk>/', views.BookDetail.as_view()),
]