from Matrix import Matrix
from random import choice, random
from recordtype import recordtype

# = ([list of id], type, amount, fitness)
Island = recordtype('Island', 'ids coordinates type amount fitness')


class IslandMatrix(Matrix):

    def __init__(self, id_matrix, figure_matrix):
        super().__init__()
        self.id_matrix = id_matrix
        self.figure_matrix = figure_matrix
        self.islands_num = 1

    def is_in_range(self, x, y, visited):
        return (0 <= y < self.height and
                0 <= x < self.width and
                not visited[y][x] and self.id_matrix[x, y])

    def is_the_same_figure(self, x, y, prev_figure):
        return prev_figure == self.figure_matrix[x, y]

    def DFS(self, x, y, visited, prev_figure, prev_num):

        rowNbr = [-1, -1, -1, 0, 0, 1, 1, 1]
        colNbr = [-1, 0, 1, -1, 1, -1, 0, 1]
        visited[y][x] = True
        self.matrix[y][x] = prev_num

        for k in range(8):
            if self.is_in_range(x + rowNbr[k], y + colNbr[k], visited):
                if self.is_the_same_figure(x + rowNbr[k], y + colNbr[k], prev_figure):
                    prev_num = self.DFS(x + rowNbr[k], y + colNbr[k], visited, prev_figure, prev_num)
                else:
                    prev_figure = self.figure_matrix[x + rowNbr[k], y + colNbr[k]]
                    prev_num = self.DFS(x + rowNbr[k], y + colNbr[k], visited, prev_figure, prev_num + 1)

        return prev_num

    def detect_islands(self):

        prev_num = 1
        visited = [[False for j in range(self.width)] for i in range(self.height)]
        self.matrix = [[0 for j in range(self.width)] for i in range(self.height)]

        for x in range(self.width):
            for y in range(self.height):
                if visited[y][x] is False and self.id_matrix[x, y] > 1:
                    prev_figure = self.figure_matrix[x, y]
                    prev_num = self.DFS(x, y, visited, prev_figure, prev_num)
                    self.islands_num = prev_num

    def calc_island_statistics(self):
        self.islands = {}
        for i in range(self.islands_num):
            # = ([list of id], [coordinates], type, amount, fittness)
            self.islands[i + 1] = Island(ids=[], coordinates=[], type=3, amount=0, fitness=0)

        for x in range(self.width):
            for y in range(self.height):
                num = self.matrix[y][x]
                type = self.figure_matrix[x, y]
                if num is not 0 and type !=0:
                    self.islands[num].ids.append(self.id_matrix[x, y])
                    self.islands[num].coordinates.append((x, y))
                    self.islands[num].type = type
                    self.islands[num].amount += 1
                    self.islands[num].fitness += type * self.islands[num].amount

    def deduce_child_type(self, id_1, id_2):
        return choice([self.islands[id_1].type, self.islands[id_2].type])

    def delete_island(self, island):
        pass

    def get_number_of_islands(self):
        return self.islands_num

    def get_islands_list(self):
        l = []
        for num in range(self.islands_num):
            l.append(num+1)
        return l

    def get_coordinates_of_given_num(self, num):
        return self.islands[num].coordinates





