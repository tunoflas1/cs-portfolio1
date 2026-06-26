"""
knight_path.py
--------------
Shortest knight path on a standard 8x8 chessboard, using breadth-first
search (BFS). BFS explores the board one "ring" of reachable squares at a
time, so the first time it reaches the target it has used the fewest moves.

Squares are written in algebraic notation, e.g. "a1", "h8".

Run from the command line:
    python knight_path.py a1 h8
"""

from collections import deque
from typing import List, Optional, Tuple

FILES = "abcdefgh"

# The eight L-shaped moves a knight can make, as (file, rank) offsets.
MOVES: List[Tuple[int, int]] = [
    (1, 2), (2, 1), (2, -1), (1, -2),
    (-1, -2), (-2, -1), (-2, 1), (-1, 2),
]


def to_coords(square: str) -> Tuple[int, int]:
    """Convert 'a1' -> (0, 0), 'h8' -> (7, 7)."""
    square = square.strip().lower()
    if len(square) != 2 or square[0] not in FILES or square[1] not in "12345678":
        raise ValueError(f"Invalid square: {square!r}")
    return FILES.index(square[0]), int(square[1]) - 1


def to_square(coords: Tuple[int, int]) -> str:
    """Convert (0, 0) -> 'a1'."""
    c, r = coords
    return f"{FILES[c]}{r + 1}"


def knight_path(start: str, target: str) -> Optional[List[str]]:
    """Return the shortest knight path from start to target, or None."""
    s = to_coords(start)
    t = to_coords(target)

    seen = {s}
    queue: deque = deque([[s]])           # queue of paths

    while queue:
        path = queue.popleft()
        c, r = path[-1]
        if (c, r) == t:
            return [to_square(p) for p in path]
        for dc, dr in MOVES:
            nc, nr = c + dc, r + dr
            if 0 <= nc < 8 and 0 <= nr < 8 and (nc, nr) not in seen:
                seen.add((nc, nr))
                queue.append(path + [(nc, nr)])
    return None


if __name__ == "__main__":
    import sys

    if len(sys.argv) == 3:
        start, target = sys.argv[1], sys.argv[2]
    else:
        start, target = "a1", "h8"

    path = knight_path(start, target)
    if path is None:
        print(f"No path from {start} to {target}.")
    else:
        print(f"{start} -> {target}: {len(path) - 1} moves (minimum)")
        print(" -> ".join(path))
