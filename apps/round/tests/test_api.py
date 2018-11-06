from django.test import TestCase

from apps.round.models import Rounds
from apps.player.models import Players


class RoundAPITests(TestCase):
    def setUp(self):
        player1, _ = Players.objects.get_or_create(username='player1')
        player2, _ = Players.objects.get_or_create(username='player2')

        round_object, _ = Rounds.objects.get_or_create(player_1=player1, player_2=player2)
        self.round_id = round_object.id

    def test_empty_usernames(self):
        post_data = {
            "player_1": "andres",
            "player_2": "",
        }

        response = self.client.post("/api/v1/rounds/", post_data)
        self.assertEquals(response.status_code, 400)
        self.assertEquals(response.data['message'], "Both player's user names are required")

    def test_equal_usernames(self):
        post_data = {
            "player_1": "andres",
            "player_2": "andres",
        }

        response = self.client.post("/api/v1/rounds/", post_data)
        self.assertEquals(response.status_code, 400)
        self.assertEquals(response.data['message'], "The player's user names should be different")

    def test_create_round(self):
        post_data = {
            "player_1": "andres",
            "player_2": "nelson",
        }

        response = self.client.post("/api/v1/rounds/", post_data)
        self.assertEquals(response.status_code, 200)

    def test_get_round(self):
        round_object = Rounds.objects.filter(player_1__username='player1', player_2__username='player2').first()

        response = self.client.get("/api/v1/rounds/{}".format(round_object.id))
        self.assertEquals(response.status_code, 200)
        print("data", response.data)
        self.assertEquals(str(round_object.id), response.data['data']['id'])
        self.assertEquals(str(round_object.player_1.username), response.data['data']['player_1']['username'])
        self.assertEquals(str(round_object.player_2.username), response.data['data']['player_2']['username'])
