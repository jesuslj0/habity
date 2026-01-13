from rest_framework.routers import DefaultRouter
from habits.views.habits import HabitViewSet

router = DefaultRouter()
router.register("habits", HabitViewSet, basename="habits")

urlpatterns = router.urls
