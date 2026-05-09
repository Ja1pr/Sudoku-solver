import math

#               Note
# This code is almost 100% made by human


class SudokuSolver:
    def __init__(self, game):
        self.game =  self.make_board(game)


    # -----Pomocné funkce-----

    def solved(self):  # Kontrola zda je sudoku vyřešeno
        for i in self.game:  # Pouze jednoduchá, kontroluje zda jsou všechna pole vyplněna
            for a in i:
                if a == 0:
                    return False
                if isinstance(a, list):
                    if a == [0]:
                        return False
        return True

    def make_board(self,game):  # Připravuje sudoku na řešení
        copya = [radek[:] for radek in game]  # Připraví si kopii na řešení, aby původní sudoku nebylo omylem poškozeno
        for y in range(len(game)):  # Projde každý řádek
            for x in range(len(game[y])):  # Prochází každé pole z řádku
                if game[y][x] == 0:
                    copya[y][x] = [0]
        return copya

    def can_place(self, x, y, n):

        for i in range(len(self.game[y])):
            if self.game[y][i] == n:
                return False
            if isinstance(self.game[y][i], list):
                if n in self.game[y][i]:
                    return False

        for j in range(len(self.game)):
            if self.game[j][x] == n:
                return False
            if isinstance(self.game[j][x], list):
                if n in self.game[j][x]:
                    return False

        grid = [math.floor(y / 3) * 3, math.floor(x / 3) * 3]
        ar = self.game[grid[0]][grid[1]:grid[1] + 3]
        br = self.game[grid[0] + 1][grid[1]:grid[1] + 3]
        cr = self.game[grid[0] + 2][grid[1]:grid[1] + 3]

        for z in range(0, 3):
            if ar[z] == n:
                return False
            if isinstance(ar[z], list):
                if n in ar[z]:
                    return False
            if br[z] == n:
                return False
            if isinstance(br[z], list):
                if n in br[z]:
                    return False
            if cr[z] == n:
                return False
            if isinstance(cr[z], list):
                if n in cr[z]:
                    return False
        return True

    def place(self, x, y):
        n = self.game[y][x][0]
        n = n + 1
        while n <= 9:
            if self.can_place(x, y, n):
                self.game[y][x] = [n]
                return True
            n = n + 1
        else:
            self.game[y][x] = [0]
            return False

    def makes_sense(self):
        for y in range(len(self.game)):
            for x in range(len(self.game[y])):
                if isinstance(self.game[y][x],int):
                    n = self.game[y][x]
                    self.game[y][x] = []
                    if not self.can_place(x, y, n):
                        return False
                    self.game[y][x] = n
        return True

    def solve(self, shared_output):
        if not self.makes_sense():
            return False
        x = 0
        y = 0
        while y<9:
            if len(shared_output) > 0:
                return None
            if isinstance(self.game[y][x], list):
                code = self.place(x, y)
                if not code:
                    if x == 0:
                        y -= 1
                        x = 8
                    else:
                        x -= 1
                    while not isinstance(self.game[y][x], list):
                        if x == 0:
                            y -= 1
                            x = 8
                        else:
                            x -= 1
                else:
                    if x == 8:
                        x = 0
                        y += 1
                    else:
                        x += 1
            else:
                if x == 8:
                    x = 0
                    y += 1
                else:
                    x += 1

            #print(f"\r{"▓" * round((x * y) * 10 / 81)}{"░" * (10 - (round((x * y) * 10 / 81)))}", end="")

        return self.game
