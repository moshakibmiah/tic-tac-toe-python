import unittest

from tic_tac_toe import WINNING_LINES, display_board, make_move, winner


class GameTests(unittest.TestCase):
    def test_every_winning_line_for_both_players(self):
        for player in ("X", "O"):
            for line in WINNING_LINES:
                board = [""] * 9
                for square in line:
                    board[square] = player
                self.assertEqual(winner(board), player)

    def test_draw(self):
        self.assertIsNone(winner(list("XOXXOOOXX")))

    def test_invalid_moves_do_not_change_board(self):
        board = ["X"] + [""] * 8
        for value in ("1", "0", "10", "hello", "1.5", ""):
            before = board.copy()
            with self.assertRaises(ValueError):
                make_move(board, value, "O")
            self.assertEqual(board, before)

    def test_valid_move_and_numbered_board(self):
        board = [""] * 9
        make_move(board, "5", "X")
        self.assertEqual(board[4], "X")
        self.assertIn("1 | 2 | 3", display_board(board))
        self.assertNotIn("5", display_board(board))


if __name__ == "__main__":
    unittest.main()
