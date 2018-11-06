import sentry_sdk

from rest_framework import status

from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.movement.controllers.movement_controller import create_movement_controller
from exceptions.generic_exceptions import GenericException


@api_view(["POST"])
def create_movement_view(request):
    """
    Create a round and return the ID or return a round incompleted created previously
    :param request: Request object.
    :return: Json, round data.
    """
    try:
        round_id = request.data['round_id']
        player_1_movement = request.data['player_1_movement']
        player_2_movement = request.data['player_2_movement']

        movement_data = create_movement_controller(round_id, player_1_movement, player_2_movement)
        return Response({'data': movement_data})

    except GenericException as e:
        return Response({'message': e.message}, status=status.HTTP_400_BAD_REQUEST)

    except Exception as e:
        sentry_sdk.capture_exception(e)
        return Response({'message': "Unexpected error creating the movement"},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)


def __validate_create_movement_view_params(data):
    if not 'player_1_movement' in data or not 'player_2_movement' in data:
        raise GenericException(message="The parameter player_1_movement and player_2_movement are required")

    player_1_movement = data['player_1_movement']
    player_2_movement = data['player_2_movement']

    if not player_1_movement or not player_2_movement:
        raise GenericException(message="Both player's movements are required")
