def get_winner_for_a_match(player_1_id, player_2_id, player_1_movement, player_2_movement):
    if player_1_movement == player_2_movement:
        return None

    if player_1_movement == "ROCK":
        if player_2_movement == "SCISSORS":
            return player_1_id
        else:
            return player_2_id

    elif player_1_movement == "PAPER":
        if player_2_movement == "ROCK":
            return player_1_id
        else:
            return player_2_id

    elif player_1_movement == "SCISSORS":
        if player_2_movement == "PAPER":
            return player_1_id
        else:
            return player_2_id
