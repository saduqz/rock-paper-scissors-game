from django.urls import path

from api.v1.movement.views import movement_view

app_name = "round"

urlpatterns = [
    path('', movement_view.create_movement_view),
]
