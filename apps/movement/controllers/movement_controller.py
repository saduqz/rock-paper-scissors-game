from exceptions.generic_exceptions import GenericException

from apps.shared.utils import get_winner_for_a_match

from apps.movement.managers.movement_manager import (
    get_round_movements_manager, create_movement_manager,
    get_round_movements_with_winner_by_user_manager
)

from apps.round.managers.round_manager import get_round_by_id_manager, set_user_as_the_winner_of_a_round


def create_movement_controller(round_id, player_1_movement, player_2_movement):
    """
    Create players controller
    :param round_id: String, movement ID.
    :param player_1_movement: String, player 1 movement.
    :param player_2_movement: String, player 2 movement.
    :return: Dictionary with created movement data.
    """
    round_data = get_round_by_id_manager(round_id)

    if round_data['winner']:
        raise GenericException(message="This round has a winner")

    winner_id = get_winner_for_a_match(round_data['player_1'], round_data['player_2'], player_1_movement,
                                       player_2_movement)

    movement = create_movement_manager(round_id, player_1_movement, player_2_movement, winner_id)

    movements_with_winner = get_round_movements_with_winner_by_user_manager(round_id, winner_id)

    if len(movements_with_winner) >= 3:
        set_user_as_the_winner_of_a_round(round_id, winner_id)

    return movement


def get_round_movements_controller(round_id):
    """
    Get round movements
    :param round_id: String, movement ID.
    :return: Dictionary with movements data into a round.
    """
    return get_round_movements_manager(round_id)
