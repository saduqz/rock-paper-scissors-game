from apps.round.managers.round_manager import (
    create_round_manager, get_last_round_by_players_name_manager, get_round_by_id_manager, get_rounds_by_round_manager
)

from apps.player.controllers.player_controller import get_or_create_players_controller


def create_round_controller(player_1, player_2):
    """
    Create round
    :param player_1: String, player 1 username.
    :param player_2: String, player 2 username.
    :return: Dictionary with round data.
    """
    player_1 = player_1.lower()
    player_2 = player_2.lower()
    get_or_create_players_controller((player_1, player_2))

    last_round = get_last_round_by_players_name_manager(player_1, player_2)
    last_round_inverse = get_last_round_by_players_name_manager(player_2, player_1)

    if last_round and not last_round['winner']:
        return last_round
    elif last_round_inverse and not last_round_inverse['winner']:
        return last_round_inverse
    else:
        round_data = create_round_manager(player_1, player_2)
        return round_data


def get_round_controller(round_id):
    """
    :param round_id: String, round ID.
    Create round
    :return: Dictionary with round data.
    """
    return get_round_by_id_manager(round_id)


def get_rounds_by_round_controller(round_id):
    """
    :param round_id: String, round ID.
    Create round
    :return: Dictionary with round data.
    """
    return get_rounds_by_round_manager(round_id)
