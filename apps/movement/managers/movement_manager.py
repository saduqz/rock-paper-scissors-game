from apps.movement.serializers.movement_serializer import MovementsSerializer

from apps.movement.models import Movements


def get_round_movements_manager(round_id):
    """
    Get round movements
    :param round_id: String, movement ID.
    :return: Dictionary with movements data into a round.
    """
    query = Movements.objects.filter(round_id=round_id).all()
    serializer = MovementsSerializer(query, many=True)
    return serializer.data


def get_round_movements_with_winner_by_user_manager(round_id, winner_id):
    """
    Get round movements
    :param round_id: String, movement ID.
    :param winner_id: String, winner ID.
    :return: Dictionary with movements data into a round.
    """
    query = Movements.objects.filter(round_id=round_id, winner_id=winner_id).all()
    serializer = MovementsSerializer(query, many=True)
    return serializer.data


def create_movement_manager(round_id, player_1_movement, player_2_movement, winner_id):
    """
    Create players controller
    :param round_id: String, movement ID.
    :param player_1_movement: String, player 1 movement.
    :param player_2_movement: String, player 2 movement.
    :param winner_id: String, winner ID or None.
    :return: Dictionary with created movement data.
    """

    movement = Movements(
        round_id=round_id,
        player_1_movement=player_1_movement,
        player_2_movement=player_2_movement,
    )

    if winner_id:
        movement.winner_id = winner_id
    movement.save()

    serializer = MovementsSerializer(movement, many=False)
    return serializer.data
