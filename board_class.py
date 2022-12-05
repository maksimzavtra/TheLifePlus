import pygame
from config import *
from random import choice


class Board:
    def __init__(self, dim, screen):
        self.x_px = dim[0]
        self.y_px = dim[1]

        self.x = self.x_px // CELL_SIZE
        self.y = self.y_px // CELL_SIZE

        self.matrix = []
        for _ in range(self.x):
            row = [(0, 0, 0)] * self.y
            self.matrix.append(row)

        self.start = False

        self.screen = screen

    def add_cell(self, xy):
        if self.matrix[xy[0]][xy[1]] == (0, 0, 0):
            self.matrix[xy[0]][xy[1]] = (255, 0, 0)
        elif self.matrix[xy[0]][xy[1]] == (255, 0, 0):
            self.matrix[xy[0]][xy[1]] = (0, 255, 0)
        elif self.matrix[xy[0]][xy[1]] == (0, 255, 0):
            self.matrix[xy[0]][xy[1]] = (0, 0, 255)
        elif self.matrix[xy[0]][xy[1]] == (0, 0, 255):
            self.matrix[xy[0]][xy[1]] = (0, 0, 0)

    def draw_cell(self, xy):
        pygame.draw.rect(self.screen, self.matrix[xy[0]][xy[1]], (xy[0] * CELL_SIZE, xy[1] * CELL_SIZE,
                                                                  CELL_SIZE, CELL_SIZE))

    def update_cell(self, x, y, alive):
        alive_count = 0
        around = []
        count = 0
        recount = 0
        for i in range(x - 1, x + 2):
            if i < 0:
                i = len(self.matrix) - 1
            elif i >= len(self.matrix):
                i = 0
            for j in range(y - 1, y + 2):
                if [i, j] != [x, y]:
                    if j < 0:
                        j = len(self.matrix[0]) - 1
                    elif j >= len(self.matrix[0]):
                        j = 0
                    if self.matrix[i][j] != (0, 0, 0):
                        alive_count += 1
                        around.append(self.matrix[i][j])
                    if self.matrix[i][j] == (255, 0, 0):
                        count += 1
                    elif self.matrix[i][j] == (0, 255, 0):
                        count -= 1
        for i in range(recount):
            if count > 0:
                count = 0 - abs(count)
            elif count < 0:
                count = abs(count)
        if alive == (0, 0, 0) and alive_count == 3:
            a = around.count((255, 0, 0))
            b = around.count((0, 255, 0))
            c = around.count((0, 0, 255))
            if a > b and a > c:
                return (0, 0, 255)
            if b > a and b > c:
                return (255, 0, 0)
            if c > a and c > b:
                return (0, 255, 0)
            return (0, 0, 255)
        if alive != (0, 0, 0) and (alive_count not in [2, 3]):
            return (0, 0, 0)
        if alive != (0, 0, 0):
            if count in [2, 3]:
                return (0, 255, 0)
            if count in [-2, -3]:
                return (0, 0, 255)
            if count in [-1, 0, 1]:
                return (255, 0, 0)
        return alive

    def turn(self):
        matrix = [i.copy() for i in self.matrix]
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                matrix[i][j] = self.update_cell(i, j, self.matrix[i][j])
        self.matrix = matrix
        self.draw_map()

    def draw_map(self):
        self.screen.fill((0, 0, 0))
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                if self.matrix[i][j] != (0, 0, 0):
                    self.draw_cell([i, j])

    def clear(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                self.matrix[i][j] = (0, 0, 0)
        self.draw_map()

    def random(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                self.matrix[i][j] = choice([(0, 0, 0), (0, 0, 0), (0, 0, 0),
                                            (0, 0, 0), (0, 0, 0), (0, 0, 0),
                                            (0, 0, 0), (0, 0, 0), (0, 0, 0),
                                            (255, 0, 0), (0, 255, 0), (0, 0, 255)])
        self.draw_map()
