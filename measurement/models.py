from django.db import models

# Модель для датчика
class Sensor(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name

# Модель для измерений температуры
class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, related_name='measurements', on_delete=models.CASCADE)
    temperature = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)  # Автоматически проставляем время создания

    def __str__(self):
        return f"{self.sensor.name}: {self.temperature}°C at {self.created_at}"
