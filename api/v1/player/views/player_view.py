from rest_framework import status

from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.player.controllers.player_controller import get_players_rank_controller
from exceptions.generic_exceptions import GenericException


@api_view(["GET"])
def get_players_rank_view(request):
    """
    Get players rank data.
    :param request: Request object.
    :return: Json, round data.
    """
    try:

        players_rank_data = get_players_rank_controller()
        return Response({'data': players_rank_data})

    except GenericException as e:
        return Response({'message': e.message}, status=status.HTTP_400_BAD_REQUEST)

    except Exception as e:
        return Response({'message': "Unexpected error getting the round"},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)
