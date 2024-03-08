import unittest
from main import TicTacToe
from custom_errors import InvalidSlotError, OccupiedSlotError

class TestTicTacToe(unittest.TestCase):

    def setUp(self):
        self.game = TicTacToe()

    def test_place_valid_moves(self):
        self.game.place('x', 1)
        self.assertIn(1, self.game.player_x, "Player X should have slot 1 occupied.")

        self.game.place('o', 2)
        self.assertIn(2, self.game.player_o, "Player O should have slot 2 occupied.")

    def test_place_invalid_slot(self):
        with self.assertRaises(InvalidSlotError):
            self.game.place('x', 10)

    def test_place_occupied_slot(self):
        self.game.place('x', 1)
        with self.assertRaises(OccupiedSlotError):
            self.game.place('o', 1)

    def test_move_valid(self):
        self.game.place('x', 1)
        self.game.move('x', 1)
        self.assertNotIn(1, self.game.player_x, "Player X should not have slot 1 after moving.")
        with self.assertRaises(ValueError):
            self.game.move('x', 1)

    def test_get_player(self):
        player_x = self.game.get_player('x')
        self.assertEqual(player_x, self.game.player_x, "Should return player X's list.")
        
        player_o = self.game.get_player('o')
        self.assertEqual(player_o, self.game.player_o, "Should return player O's list.")
        
        with self.assertRaises(ValueError):
            self.game.get_player('z')

if __name__ == '__main__':
    unittest.main()
