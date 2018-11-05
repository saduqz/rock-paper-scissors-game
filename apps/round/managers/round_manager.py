from apps.round.serializers.round_serializer import RoundSerializer

from apps.round.models import Rounds
from apps.player.models import Players


def create_round_manager(player_1, player_2):
    """
    Get round objects.
    :return: Dictionary, serializer with logbook data.
    """
    player_1 = Players.objects.get(username=player_1)
    player_2 = Players.objects.get(username=player_2)

    round = Rounds(player_1=player_1, player_2=player_2)
    round.save()

    serializer = RoundSerializer(round, many=False)
    return serializer.data


def get_last_round_by_players_name_manager(player_1, player_2):
    """
    Get round objects.
    :return: Dictionary, serializer with logbook data.
    """

    query = Rounds.objects.filter(player_1__username=player_1, player_2__username=player_2)
    query = query.order_by('-created_at')

    if query.first():
        serializer = RoundSerializer(query.first(), many=False)
        return serializer.data
    else:
        return None


def get_round_by_id_manager(round_id):
    """
    Get round objects.
    :param round_id: String, movement ID.
    :return: Dictionary, serializer with logbook data.
    """

    query = Rounds.objects.filter(id=round_id).first()
    serializer = RoundSerializer(query, many=False)
    return serializer.data


def set_user_as_the_winner_of_a_round(round_id, user_id):
    """
    Set an user as the winner of a round
    :param round_id: String, movement ID.
    :param user_id: String, User ID.
    :return: Dictionary with Round data.
    """
    round_object = Rounds.objects.get(id=round_id)
    round_object.winner_id = user_id
    round_object.save()

    serializer = RoundSerializer(round_object, many=False)
    return serializer.data
