from rest_framework import serializers
from .models import RouteModel


class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = RouteModel
        fields = '__all__'
