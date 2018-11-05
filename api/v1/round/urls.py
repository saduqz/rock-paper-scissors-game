from django.urls import path

from api.v1.round.views import round_view

app_name = "round"

urlpatterns = [
    path('', round_view.create_round_view),
    path('<round_id>', round_view.get_round_view),
    path('<round_id>/all-rounds', round_view.get_rounds_by_round),
]
