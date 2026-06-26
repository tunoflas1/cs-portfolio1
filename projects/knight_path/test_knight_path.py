"""
test_knight_path.py
-------------------
Minimal tests for the knight path finder. Run with:
    python -m unittest test_knight_path.py
"""

import unittest
from knight_path import knight_path, to_coords, to_square


class TestKnightPath(unittest.TestCase):

    def test_same_square(self):
        self.assertEqual(knight_path("d4", "d4"), ["d4"])

    def test_single_move(self):
        # b1 -> c3 is one legal knight move.
        path = knight_path("b1", "c3")
        self.assertEqual(len(path) - 1, 1)

    def test_corner_to_corner(self):
        # a1 -> h8 is a well-known 6-move trip.
        path = knight_path("a1", "h8")
        self.assertEqual(len(path) - 1, 6)

    def test_path_is_continuous(self):
        path = knight_path("a1", "h8")
        for a, b in zip(path, path[1:]):
            ca, ra = to_coords(a)
            cb, rb = to_coords(b)
            self.assertIn((abs(ca - cb), abs(ra - rb)), {(1, 2), (2, 1)})

    def test_round_trip_notation(self):
        self.assertEqual(to_square(to_coords("f6")), "f6")

    def test_invalid_square(self):
        with self.assertRaises(ValueError):
            knight_path("z9", "a1")


if __name__ == "__main__":
    unittest.main()
