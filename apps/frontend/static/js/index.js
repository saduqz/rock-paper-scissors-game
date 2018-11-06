let app = new Vue({
  el: "#app",
  data: {
    message: "Hello Vue!",
    isInGame: false,
    rock_paper_scissors_image: "/static/img/rock-paper-scissors.jpg",
    roundNumber: 1,
    roundId: null,
    player1: "",
    player2: "",
    movementPlayer1: "ROCK",
    movementPlayer2: "ROCK",
    rounds: [],
    roundMovements: [],
    disableOkButton: false,
    playersRank: []
  },
  mounted() {
    this.getPlayersrank();
  },
  methods: {
    getPlayersrank: function() {
      apiGetPlayersRank().then(data => {
        this.playersRank = data;
      });
    },
    startToPlay: function() {
      if (this.player1 && this.player2 && this.player1 !== this.player2) {
        this.isInGame = true;
        apiCreateRound(this.player1, this.player2).then(data => {
          if (data.player_1.username !== this.player1) {
            this.player1 = data.player_1.username;
            this.player2 = data.player_2.username;
          }
          this.roundId = data.id;
          this.roundMovements = data.movements_set;
          this.updateRoundsData();
        });
      } else {
        toastr.error("Players are required and can't be equals");
      }
    },
    createMovement: function() {
      this.disableOkButton = true;
      apiCreateMovement(
        this.roundId,
        this.movementPlayer1,
        this.movementPlayer2
      ).then(data => {
        if (data.round_finished) {
          this.getPlayersrank();
          apiCreateRound(this.player1, this.player2).then(newRound => {
            this.roundId = newRound.id;
            this.roundMovements = newRound.movements_set;
            this.updateRoundsData();
            this.disableOkButton = false;
            let message = `The winner for the round ${this.roundNumber} is ${
              data.winner.username
            }`;
            toastr.info(message);
          });
        } else {
          apiGetRoundData(this.roundId).then(data => {
            this.roundMovements = data.movements_set;
            this.disableOkButton = false;
          });
        }
      });
    },
    cancel: function() {
      this.isInGame = false;
      this.clearData();
    },

    updateRoundsData: function() {
      apiGetRoundsDataByRound(this.roundId).then(data => {
        this.rounds = data;
        this.roundNumber = data.length;
      });
    },
    clearData: function() {
      this.player1 = "";
      this.player2 = "";
      this.movementPlayer1 = "ROCK";
      this.movementPlayer2 = "ROCK";
      this.rounds = [];
      this.disableOkButton = false;
    },
  }
});
