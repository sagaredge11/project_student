
from rest_framework.serializers import ModelSerializer

from .models import Student


class stu_ser(ModelSerializer):
    class Meta:
        model=Student
        fields='__all__'

