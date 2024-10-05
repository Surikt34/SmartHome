from django.urls import path
from .views import SensorView, MeasurementView, SensorsListView, SensorDetailView

urlpatterns = [
    path('sensors/', SensorsListView.as_view(), name='sensors-list'),  # Список датчиков
    path('sensors/<int:pk>/', SensorDetailView.as_view(), name='sensor-detail'),  # Детальная информация о датчике
    path('sensor/', SensorView.as_view(), name='sensor-create'),  # Создание нового датчика
    path('sensor/<int:pk>/', SensorView.as_view(), name='sensor-update'),  # Обновление датчика
    path('measurement/', MeasurementView.as_view(), name='measurement-create'),  # Добавление нового измерения
]