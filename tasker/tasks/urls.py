from django.conf.urls import url
from django.urls import path
from rest_framework_mongoengine import routers
from .views import TaskViewSet, CreateTask

router = routers.DefaultRouter()
router.register(r'mongo', TaskViewSet)

urlpatterns = [
 path('create/', CreateTask.as_view(), name='create'),
]

urlpatterns += router.urls