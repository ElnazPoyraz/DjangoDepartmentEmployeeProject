from django.urls import path
from .views import DepartmanMVS, PersonelMVS
from rest_framework import routers

router = routers.DefaultRouter()
router.register("departman", DepartmanMVS)
router.register("personel", PersonelMVS)

urlpatterns = [
   
] + router.urls
