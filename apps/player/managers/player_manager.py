from apps.player.serializers.player_serializer import PlayerSerializer

from apps.player.models import Players


def get_or_create_players_manager(usernames):
    """
    Create player manager.
    :param usernames: List, players username. e.g ["andres", "nelson"]
    :return: Dictionary, serializer with player data.
    """
    data = []

    for username in usernames:
        player, was_created = Players.objects.get_or_create(username=username)
        data.append(player)

    serializer = PlayerSerializer(data, many=True)
    return serializer.data


def get_players_rank_manager():
    """
    Get players rank data sorted by rounds won descending
    :return: List with players rank data.
    """
    query = Players.objects.prefetch_related('rounds_set').all()
    serializer = PlayerSerializer(query, many=True)
    return serializer.data
