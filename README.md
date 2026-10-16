# Sudoku solver

!SOLVER v3 was not yet translated into .exe! If you want to use newst version, you have to use the .px

New version of Solver that uses MRV to be more effective and faster

This sudoku solver can solve any sudoku (if it is valid) under 5 seconds!
Time table:

Classic sudokus................ < 1 second (this reamined unchanged across versions)
                     
World hardest sudokus.... < 1 seconds 


17-clues sudokus............. < 1 seconds (major upgrade, version 2: 7 seconds,  version 1: 30 second)

unsolvable sudokus - This new version handles them really well, while older vesions could get stuck

In some rare cases ultra-hard sudokos can take up to 30 seconds, but this should be fixed with newest version


All code wrote in python

Method: Bactracking with 8 cores racing to solve it form different sides and mirrors and MRV
