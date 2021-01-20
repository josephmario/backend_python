from django.urls import path, include
from .views import InfoCustomerViewSet, UserViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('infocustomer', InfoCustomerViewSet, basename='infocustomer')
router.register('users', UserViewSet)

urlpatterns = [
	path('api/', include(router.urls)),
	# path('viewset/', include(router.urls)),
	# path('viewset/<int:pk>/', include(router.urls)),
]
