# Sudoku Solver

A fast Python sudoku solver that handles everything from classic puzzles to the hardest known grids, typically in well under 5 seconds.

> **Note:** Solver v3 has not been compiled into an `.exe` yet. To use the newest version, run the `.py` file directly.

## What's new in v3
- **MRV heuristic** (Minimum Remaining Values): always fills the cell with the fewest candidates first, which prunes the search tree dramatically.
- **Better handling of unsolvable puzzles**: invalid grids are detected and rejected instead of getting the solver stuck, as happened in older versions.
- **Ultra-hard puzzles** that could previously take up to 30 seconds should now be solved much faster.

## Performance

| Puzzle type            | v1       | v2       | v3 (current) |
|------------------------|----------|----------|--------------|
| Classic sudokus        | < 1 s    | < 1 s    | < 1 s        |
| World's hardest sudokus| –        | –        | < 1 s        |
| 17-clue sudokus        | ~30 s    | ~7 s     | < 1 s        |
| Unsolvable sudokus     | may hang | –        | handled quickly |

Any valid sudoku is solved in under 5 seconds.

## How it works
The solver uses **backtracking with MRV**, running **8 parallel processes** (one per core). Each process attacks the puzzle from a different direction (original grid and mirrored/rotated variants), and the first one to find a solution wins and stops the others.

## Tech
- Language: Python (100 %)
- Parallelism: multiprocessing (8 workers)

