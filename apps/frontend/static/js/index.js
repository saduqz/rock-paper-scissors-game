let app = new Vue({
    el: '#app',
    data: {
        message: 'Hello Vue!',
        isInGame: false,
        rock_paper_scissors_image: "/static/img/rock-paper-scissors.jpg",
        round_number: 1,
        player1: "",
        player2: "",
        selectPlayer1: "ROCK",
        selectPlayer2: "ROCK",
        rounds: [],
    },
    methods: {
        start: function () {
            if (this.player1 && this.player2) {
                this.isInGame = true;
                this.test();
            } else {
                alert("Players are required")
            }
        },
        cancel: function () {
            this.isInGame = false;
            this.clearData();
        },
        clearData: function () {
            this.player1 = "";
            this.player2 = "";
            this.rounds = [];
        },

        test: function () {
            this.player1 = "Andrés";
            this.player2 = "Nelson";
            console.log("selectPlayer1: ", this.selectPlayer1);
            console.log("selectPlayer2: ", this.selectPlayer2);

            this.rounds = [
                {number: 1, winner: "Andrés"},
                {number: 2, winner: "Andrés"},
                {number: 3, winner: "Nelson"},
                {number: 4, winner: "Nelson"},
                {number: 5, winner: "Andrés"},
            ]
        },
    }
});
