# Sudoku solver

Newest version brings major speed up! It utilizes multiprocessing library instead of threading
This sudoku solver can solve any sudoku (if it is valid) under 30 seconds!
Time table:

Classic sudokus................ < 1 second (this reamined unchanged across versions)
                     
World hardest sudokus.... < 1 seconds (althought thre real time is about 5 seconds because the cores are initiating)



17-clues sudokus............. < 7 seconds (major upgrade, older version 30 second)

unsolvable sudokus - This new version handles them really well, while older vesions could get stuck

In some rare cases ultra-hard sudokos can take up to 30 seconds, but this should be fixed with newest version


All code wrote in python

Method: Bactracking with 8 cores racing to solve it form different sides and mirrors
