from rest_framework_swagger.views import get_swagger_view
from django.urls import path, include

app_name = "api"

schema_view = get_swagger_view(title='Rock Paper Scissors Game')

urlpatterns = [
    path('docs/', schema_view),
    path('v1/', include('api.v1.urls', namespace='v1')),
]
