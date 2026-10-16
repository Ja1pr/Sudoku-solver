# WARNING - Compatible with frontend coreripper.py & Multiprocessing GUI

import time
class SudokuSolver:
    def __init__(self, game):
        self.game = game
    def solved(self):
        return not any(0 in radek for radek in self.game)
    def can_place(self, x, y, n):
        for i in range(9):
            if self.game[y][i] == n or self.game[i][x] == n:
                return False
        start_y, start_x = (y // 3) * 3, (x // 3) * 3
        for z in range(3):
            for c in range(3):
                if self.game[start_y + z][start_x + c] == n:
                    return False
        return True
    def place(self, x, y):
        n = self.game[y][x] + 1
        while n <= 9:
            if self.can_place(x, y, n):
                self.game[y][x] = n
                return True
            n += 1
        self.game[y][x] = 0
        return False
    def makes_sense(self):
        for y in range(len(self.game)):
            for x in range(len(self.game[y])):
                if  self.game[y][x] != 0:
                    n = self.game[y][x]
                    self.game[y][x] = 0
                    if not self.can_place(x, y, n):
                        self.game[y][x] = n
                        return False
                    self.game[y][x] = n
        return True
    def best(self):
        low,ly,lx = 10,None,None
        for y in range(9):
            for x in range(9):
                if self.game[y][x] == 0:
                    can = 0
                    for i in range(1, 10):
                        if self.can_place(x, y, i):
                            can += 1
                    if can == 0:return -1,-1
                    if can==1:return y,x
                    if can<low:
                        low,ly,lx = can,y,x
        return ly,lx
    def solve(self, stop_flag, queue, id_procesu):
        if not self.makes_sense():
            return False
        history = []
        steps = 0
        start_time = time.time()
        last_report_time = start_time
        while not self.solved():
            if stop_flag.value == 1:
                return False
            y, x = self.best()
            if y==-1:
                if not history:
                    break
                else:
                    failed = 0
                    bx, by = history.pop()
                    while not self.place(bx,by):
                        if not history:
                            failed = 1
                            break
                        else:
                            bx, by = history.pop()
                    if not failed:
                        history.append((bx,by))
            else:
                self.place(x, y)
                history.append((x, y))

            # AI
            steps += 1
            current_time = time.time()
            if current_time - last_report_time >= 0.1:
                elapsed = current_time - start_time
                speed = steps / elapsed if elapsed > 0 else 0
                queue.put(("report", (id_procesu, steps, speed)))
                last_report_time = current_time
        return self.game
