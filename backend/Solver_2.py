import time
#               Note
# WARNING - This code is compatible only with frontend coreripper.py (and it´s versions)
# This code is almost 100% made by human
# Programmers: Ja1pr
# Optimizing consulted with AI

class SudokuSolver:
    def __init__(self, game):
        self.game = game
        self.mask = self.make_board()

    def solved(self):
        if 0 in self.game: return False
        return True

    def make_board(self):
        copya = [radek[:] for radek in self.game]
        for y in range(len(self.game)):
            for x in range(len(self.game[y])):
                if self.game[y][x] != 0: copya[y][x] = 1
        return copya

    def can_place(self, x, y, n):
        for i in range(9):
            if self.game[y][i] == n or self.game[i][x] == n: return False
        start_y, start_x = (y // 3) * 3, (x // 3) * 3
        for z in range(3):
            for c in range(3):
                if self.game[start_y + z][start_x + c] == n: return False
        return True

    def place(self, x, y):
        n = self.game[y][x] + 1
        while n <= 9:
            if self.can_place(x, y, n):
                self.game[y][x] = n
                return True
            n = n + 1
        self.game[y][x] = 0
        return False

    def makes_sense(self):
        for y in range(len(self.game)):
            for x in range(len(self.game[y])):
                if self.mask[y][x] == 1:
                    n = self.game[y][x]
                    self.game[y][x] = 0
                    if not self.can_place(x, y, n): return False
                    self.game[y][x] = n
        return True

    # Přidán parametr queue
    def solve(self, stop_flag, queue, id_procesu=1):
        if not self.makes_sense():
            return False
        x, y = 0, 0

        krok = 0
        start_casu_jadra = time.time()
        posledni_update = time.time()

        while y < 9:
            krok += 1

            if krok % 20000 == 0:
                if hasattr(stop_flag, 'value') and stop_flag.value == 1:
                    return None

            aktualni_cas = time.time()
            if aktualni_cas - posledni_update >= 0.5:  # <--- Každých 0.5 vteřiny pošle report
                vteriny = aktualni_cas - start_casu_jadra
                rychlost = krok / vteriny if vteriny > 0 else 0
                queue.put(("report", (id_procesu, krok, rychlost)))
                posledni_update = aktualni_cas  # Resetujeme časovač pro report

            if self.mask[y][x] != 1:
                code = self.place(x, y)
                if not code:
                    while True:
                        if x == 0:
                            y -= 1
                            x = 8
                        else:
                            x -= 1
                        if y < 0: return False
                        if self.mask[y][x] != 1: break
                    continue
            if x == 8:
                x = 0; y += 1
            else:
                x += 1

        return self.game
