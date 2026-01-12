from django.urls import path,include
from rest_framework.routers import DefaultRouter
from borrowing.views import BookCopyViewSet,BorrowingViewSet


router = DefaultRouter()
router.register('BookCopy',BookCopyViewSet)
router.register('Borrowing',BorrowingViewSet)


urlpatterns = [
    path("",include(router.urls))
]