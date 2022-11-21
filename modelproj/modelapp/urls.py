
from django.urls import path, include
from rest_framework import routers

from .views import stu_view

naresh=routers.DefaultRouter()
naresh.register(r'stu_view',stu_view,basename="stu_view")
urlpatterns = [
    path('',include(naresh.urls)),

]


