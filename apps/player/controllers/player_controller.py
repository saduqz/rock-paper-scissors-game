from apps.player.managers.player_manager import get_or_create_players_manager, get_players_rank_manager


def get_or_create_players_controller(usernames):
    """
    Create players controller
    :param usernames:
    :return: Dictionary players data
    """
    return get_or_create_players_manager(usernames)


def get_players_rank_controller():
    return get_players_rank_manager()
