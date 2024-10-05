from rest_framework import serializers
from .models import Sensor, Measurement

# Сериализатор для измерений температуры
class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['sensor','temperature', 'created_at']

# Сериализатор для отображения списка датчиков
class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description']

# Сериализатор для отображения детальной информации о датчике
class SensorDetailSerializer(serializers.ModelSerializer):
    measurements = MeasurementSerializer(read_only=True, many=True)

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']