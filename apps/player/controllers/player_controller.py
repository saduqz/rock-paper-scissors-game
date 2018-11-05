from operator import itemgetter

from apps.player.managers.player_manager import get_or_create_players_manager, get_players_rank_manager


def get_or_create_players_controller(usernames):
    """
    Create players controller
    :param usernames:
    :return: Dictionary players data
    """
    return get_or_create_players_manager(usernames)


def get_players_rank_controller():
    """
    Get players rank data sorted by rounds won descending
    :return: List with players rank data.
    """
    data = get_players_rank_manager()
    data = sorted(data, key=itemgetter('rounds_won'), reverse=True)

    return data
