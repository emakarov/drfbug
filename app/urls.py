from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from app import views

router = DefaultRouter()
router.register(r'note', views.NoteViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
