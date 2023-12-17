from rest_framework import routers

from decks.views import DeckViewSet

router = routers.SimpleRouter()

router.register(r'', DeckViewSet)

urlpatterns = router.urls
