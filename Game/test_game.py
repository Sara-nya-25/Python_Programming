import unittest
from Fruit_loop.grid import Grid
from Fruit_loop.player import Player

class TestGridGame(unittest.TestCase):

    def setUp(self):
        """Standard setup for each test."""
        self.grid = Grid()
        self.player = Player(5, 5)
        self.grid.set_player(self.player)

    ## --- Grid Tests ---

    def test_grid_initialization(self):
        """Ensure grid starts with correct dimensions and is empty."""
        self.assertEqual(len(self.grid.data), 12) # height
        self.assertEqual(len(self.grid.data[0]), 36) # width
        self.assertEqual(self.grid.get(0, 0), ".")

    def test_make_walls(self):
        """Verify outer walls are placed correctly."""
        self.grid.make_walls()
        # Check corners
        self.assertEqual(self.grid.get(0, 0), "■")
        self.assertEqual(self.grid.get(35, 11), "■")
        # Check middle (should still be empty)
        self.assertEqual(self.grid.get(18, 6), ".")

    def test_is_in_bounds(self):
        """Verify boundary detection."""
        self.assertTrue(self.grid.is_in_bounds(0, 0))
        self.assertTrue(self.grid.is_in_bounds(35, 11))
        self.assertFalse(self.grid.is_in_bounds(-1, 0))
        self.assertFalse(self.grid.is_in_bounds(36, 12))

    ## --- Player Movement Tests ---

    def test_player_can_move_empty(self):
        """Player should move into empty space."""
        # Can move Right (dx=1, dy=0)
        self.assertTrue(self.player.can_move(1, 0, self.grid))

    def test_player_cannot_move_into_wall(self):
        """Player should be blocked by walls."""
        self.grid.set(6, 5, "■") # Wall to the right of player (5,5)
        self.assertFalse(self.player.can_move(1, 0, self.grid))

    ## --- Jump Logic Tests ---

    def test_successful_jump(self):
        """Player should jump over one tile and land on the second."""
        # Starting at 5,5. Jump Right (dx=1) should land at 7,5.
        success = self.player.jump(1, 0, self.grid)
        self.assertTrue(success)
        self.assertEqual(self.player.pos_x, 7)
        self.assertEqual(self.player.pos_y, 5)

    def test_failed_jump_out_of_bounds(self):
        """Player should not be able to jump off the map."""
        self.player.pos_x = 35 # Edge of width
        success = self.player.jump(1, 0, self.grid)
        self.assertFalse(success)
        self.assertEqual(self.player.pos_x, 35) # Position shouldn't change

    def test_jump_landing_on_wall(self):
        """Player cannot jump if the landing tile is a wall."""
        self.grid.set(7, 5, "■") # Wall 2 spaces to the right
        success = self.player.jump(1, 0, self.grid)
        self.assertFalse(success)
        self.assertEqual(self.player.pos_x, 5) # Position shouldn't change

    ## --- Randomized Placement Tests ---

    def test_place_exit(self):
        """Ensure an exit 'E' is actually placed on the grid."""
        self.grid.place_exit()
        # Flatten the grid data to search for 'E'
        flat_grid = [item for row in self.grid.data for item in row]
        self.assertIn("E", flat_grid)

if __name__ == '__main__':
    unittest.main()

"""
Test Results:
=============================================== test session starts ================================================
platform win32 -- Python 3.14.0, pytest-9.0.2, pluggy-1.6.0 -- C:\Python314\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\Elev\PycharmProjects\Python_Programming
configfile: pytest.ini
collected 9 items                                                                                                   

Game/test_game.py::TestGridGame::test_failed_jump_out_of_bounds PASSED                                        [ 11%]
Game/test_game.py::TestGridGame::test_grid_initialization PASSED                                              [ 22%]
Game/test_game.py::TestGridGame::test_is_in_bounds PASSED                                                     [ 33%]
Game/test_game.py::TestGridGame::test_jump_landing_on_wall PASSED                                             [ 44%]
Game/test_game.py::TestGridGame::test_make_walls PASSED                                                       [ 55%]
Game/test_game.py::TestGridGame::test_place_exit PASSED                                                       [ 66%]
Game/test_game.py::TestGridGame::test_player_can_move_empty PASSED                                            [ 77%]
Game/test_game.py::TestGridGame::test_player_cannot_move_into_wall PASSED                                     [ 88%]
Game/test_game.py::TestGridGame::test_successful_jump PASSED                                                  [100%]

================================================ 9 passed in 0.10s =================================================
"""