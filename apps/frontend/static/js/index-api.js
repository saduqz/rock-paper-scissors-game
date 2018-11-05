function apiCreateMovement(round_id, movementPlayer1, movementPlayer2) {
  return axios
    .post("/api/v1/movements/", {
      round_id: round_id,
      player_1_movement: movementPlayer1,
      player_2_movement: movementPlayer2
    })
    .then(response => {
      return response.data.data;
    });
}

function apiCreateRound(player1, player2) {
  return axios
    .post("/api/v1/rounds/", {
      player_1: player1,
      player_2: player2
    })
    .then(response => {
      return response.data.data;
    });
}

function apiGetRoundData(roundId) {
  return axios.get(`/api/v1/rounds/${roundId}`).then(response => {
    return response.data.data;
  });
}

function apiGetRoundsDataByRound(roundId) {
  return axios.get(`/api/v1/rounds/${roundId}/all-rounds`).then(response => {
    return response.data.data;
  });
}

function apiGetPlayersRank(roundId) {
  return axios.get(`/api/v1/players/rank`).then(response => {
    return response.data.data;
  });
}
