from rest_framework import status

from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.round.controllers.round_controller import create_round_controller, get_round_controller
from exceptions.generic_exceptions import GenericException


@api_view(["POST"])
def create_round_view(request):
    """
    Create a round and return the ID or return a round uncompleted created previously
    :param request: Request object.
    :return: Json, round data.
    """
    try:

        player_1 = request.data['player_1']
        player_2 = request.data['player_2']

        round_data = create_round_controller(player_1, player_2)
        return Response({'data': round_data})

    except GenericException as e:
        return Response({'message': e.message}, status=status.HTTP_400_BAD_REQUEST)

    except Exception as e:
        return Response({'message': "Unexpected error creating the round"},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["GET"])
def get_round_view(request, round_id):
    """
    Get a round data
    :param request: Request object.
    :param round_id: Round ID.
    :return: Json, round data.
    """
    try:

        round_data = get_round_controller(round_id)
        return Response({'data': round_data})

    except GenericException as e:
        return Response({'message': e.message}, status=status.HTTP_400_BAD_REQUEST)

    except Exception as e:
        return Response({'message': "Unexpected error getting the round"},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)
