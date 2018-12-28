from Figures import Figures
from consts import *
from random import choice, getrandbits, random


class DrawingManager:

    def __init__(self):
        self.f = Figures()

    @staticmethod
    def is_point_in_range(x, y):
        if x > X_MAX or x < 0 or y > Y_MAX or y < 0:
            return False
        return True

    def __count_next_pivot(self):
        while True:
            x, y = self.f.random_pivot
            new_x = x + 2 * RADIUS * getrandbits(1) * choice([-1, 1])
            new_y = y + 2 * RADIUS * getrandbits(1) * choice([-1, 1])
            if self.is_point_in_range(new_x, new_y) and (not (new_x, new_y) in self.f.pivots):
                print("NEW PAIR: {}  :  {}".format(new_x, new_y))
                return new_x, new_y

    def prepare_new_random_figure(self):
        pivot_pos = self.__count_next_pivot()
        r = random()
        pol = self.f.polygons_data
        for k, v in pol.items():
            if v.wheel_range[0] < r < v.wheel_range[1]:
                verticles_count = int(k)
                self.f.add(pivot=pivot_pos, figure_type=verticles_count)

    @property
    def elements_num(self):
        return len(self.f.shapes)

    @property
    def pivots(self) -> list:
        return self.f.pivots

    @property
    def figure_types(self) -> list:
        return self.f.figure_types

    @property
    def number_of_all_verticles(self):
        return self.f.number_of_all_verticles

