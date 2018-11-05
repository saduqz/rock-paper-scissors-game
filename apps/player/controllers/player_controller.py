from apps.player.managers.player_manager import get_or_create_players_manager


def get_or_create_players_controller(usernames):
    """
    Create players controller
    :param usernames:
    :return: Dictionary players data
    """
    return get_or_create_players_manager(usernames)
