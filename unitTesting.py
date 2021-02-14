import unittest
from tictactoe import TicTacToe
class TestStringMethods(unittest.TestCase):
    def setUp(self):
        self.ttt = TicTacToe()
        self.board = self.ttt.board
    def test_invalid_move(self):
        self.board[0][0]='x'
        self.assertEqual(self.ttt.valid_move('o', 0, 0), False)
    def test_valid_move(self):
        self.assertEqual(self.ttt.valid_move('x', 0, 0), True)
    def test_place_marker(self):
        self.assertEqual(self.ttt.place_marker('x', 0, 0), True)
    def test_place_marker_less_than_zero(self):
        self.assertEqual(self.ttt.place_marker('x', -1, 0), False)
    def test_place_marker_out_of_bound(self):
        self.assertEqual(self.ttt.place_marker('o', 3, 0), False)
    def test_place_marker_overlap(self):
        self.board[0][0] = 'x'
        self.assertEqual(self.ttt.place_marker('o', 0, 0), False)

    def test_valid_game_checker_row_1_winner(self):
        self.board[0][0] = self.board[0][1] = self.board[0][2] = 'x'
        self.assertEqual(self.ttt.game_checker('x'), True)
    def test_valid_game_checker_row_2_winner(self):
        self.board[1][0] = self.board[1][1] = self.board[1][2] = 'x'
        self.assertEqual(self.ttt.game_checker('x'), True)
    def test_valid_game_checker_row_3_winner(self):
        self.board[2][0] = self.board[2][1] = self.board[2][2] = 'x'
        self.assertEqual(self.ttt.game_checker('x'), True)

    def test_valid_game_checker_col_1_winner(self):
        self.board[0][0] = self.board[1][0] = self.board[2][0] = 'x'
        self.assertEqual(self.ttt.game_checker('x'), True)

    def test_valid_game_checker_col_2_winner(self):
        self.board[0][1] = self.board[1][1] = self.board[2][1] = 'x'
        self.assertEqual(self.ttt.game_checker('x'), True)
    def test_valid_game_checker_col_3_winner(self):
        self.board[0][2] = self.board[1][2] = self.board[2][2] = 'o'
        self.assertEqual(self.ttt.game_checker('o'), True)

    def test_valid_game_checker_diagonal1_winner(self):
        self.board[0][0] = self.board[1][1] = self.board[2][2] = 'x'
        self.assertEqual(self.ttt.game_checker('x'), True)
    def test_valid_game_checker_diagonal2_winner(self):
        self.board[0][2] = self.board[1][1] = self.board[2][0] = 'o'
        self.assertEqual(self.ttt.game_checker('o'), True)

    def test_invalid_game_checker_wrong_symbol(self):
        self.board[0][2] = self.board[1][2] = self.board[2][2] = 'x'
        self.assertEqual(self.ttt.game_checker('o'), False)

    def test_invalid_game_checker(self):
        self.board[0][2] = self.board[1][2] = 'o'
        self.assertEqual(self.ttt.game_checker('o'), False)

    def test_x_winner_checker(self):
        self.ttt.place_marker('x',0,2)
        self.ttt.place_marker('x',1,2)
        self.ttt.place_marker('x',2,2)
        self.assertEqual(self.ttt.winner_checker('x'), "Game won by x")

    def test_o_winner_checker(self):
        self.ttt.place_marker('o',0,1)
        self.ttt.place_marker('o',1,1)
        self.ttt.place_marker('o',2,1)
        self.assertEqual(self.ttt.winner_checker('o'), "Game won by o")

    def test_draw_winner_checker(self):
        self.ttt.place_marker('x',1,1)
        self.ttt.place_marker('x',2,1)
        self.ttt.place_marker('x',1,2)
        self.ttt.place_marker('x',0,0)
        self.ttt.place_marker('o',0,1)
        self.ttt.place_marker('o',0,2)
        self.ttt.place_marker('o',1,0)
        self.ttt.place_marker('o',2,2)
        self.ttt.place_marker('o',2,0)
        self.assertEqual(self.ttt.winner_checker('x'), "Game is a draw")
    def test_reset_board(self):
        self.ttt.place_marker('x',1,1)
        self.ttt.reset()
        self.assertEqual(self.ttt.board[1][1],'_')
    def test_reset_cross_turn(self):
        self.ttt.place_marker('x',1,1)
        self.ttt.reset()
        self.assertEqual(self.ttt.STATES.CROSS_TURN,0)

    def test_reset_naught_turn(self):
        self.ttt.place_marker('o',1,1)
        self.ttt.reset()
        self.assertEqual(self.ttt.STATES.NAUGHT_TURN,0)

if __name__ == '__main__':
    unittest.main()
