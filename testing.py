import unittest
from wcFeaturesFunctions import worldCupTeams
from betting import betting_odds
from wcFeaturesFunctions import findTeamId




class TestWorldCup(unittest.TestCase):

    def test_worldCup_teams(self):
        my_type = type(worldCupTeams())
        self.assertEqual(my_type, list)

    def test_teamFinished(self):
        message = betting_odds("Brazil")
        self.assertEqual(message, "Team has played their final group stage match, no odds available")

    def test_teamID(self):
        result = findTeamId("Italy", [])
        self.assertEqual(result, None)


    

        