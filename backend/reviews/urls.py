from django.urls import path,include
from rest_framework.routers import DefaultRouter
from reviews.views import ReviewsViewSet


router = DefaultRouter()
router.register('Reviews',ReviewsViewSet)


urlpatterns = [
    path("",include(router.urls))
]