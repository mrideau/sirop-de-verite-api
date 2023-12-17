from rest_framework import routers

from choices.views import ChoicesViewSet

router = routers.SimpleRouter()

router.register(r'', ChoicesViewSet)

urlpatterns = router.urls
