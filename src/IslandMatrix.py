from Matrix import Matrix
from consts import X_MAX, Y_MAX, RADIUS
from random import choice, shuffle
from recordtype import recordtype

# = ([list of id], type, amount, fittness)
Island = recordtype('Island', 'ids type amount fitness')


class IslandMatrix(Matrix):

    def __init__(self, idMatrix, figure_matrix):
        super().__init__()
        self.idMatrix = idMatrix
        self.figure_matrix = figure_matrix
        self.islands_num = 1

    def isSafe(self, x, y, visited):
        return (0 <= y < self.height and
                0 <= x < self.width and
                not visited[y][x] and self.idMatrix[x, y])

    def is_the_same_figure(self, x, y, prev_figure):
        return prev_figure == self.figure_matrix[x, y]

    def DFS(self, x, y, visited, prev_figure, prev_num):

        rowNbr = [-1, -1, -1, 0, 0, 1, 1, 1]
        colNbr = [-1, 0, 1, -1, 1, -1, 0, 1]
        visited[y][x] = True
        self.matrix[y][x] = prev_num

        for k in range(8):
            if self.isSafe(x + rowNbr[k], y + colNbr[k], visited):
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
                if visited[y][x] is False and self.idMatrix[x, y] > 1:
                    prev_figure = self.figure_matrix[x, y]
                    prev_num = self.DFS(x, y, visited, prev_figure, prev_num)

        self.islands_num = prev_num

    def calc_island_statistics(self):
        islands = {}
        for i in range(self.islands_num):
            # = ([list of id], type, amount, fittness)
            islands[i + 1] = Island(ids=[], type=3, amount=0, fitness=0)

        for x in range(self.width):
            for y in range(self.height):
                num = self.matrix[y][x]
                type = self.figure_matrix[x, y]
                if num is not 0 and type !=0:
                    islands[num].ids.append(num)
                    islands[num].type = type
                    islands[num].amount += 1
                    islands[num].fitness += type * islands[num].amount

    def deduce_child_type(self, id_1, id_2):
        return choice([self.islands[id_1], self.islands[id_2]])

    def delete_island(self):
        pass

    def get_number_of_islands(self):
        return self.islands_num

    # def calc_fitness_function(self):
    #     for i in range(self.islands_num):
    #     return 0

# def get_free_space(self, first_parent_pivot,  size=3):
#     new_free_space = []
#     f_x, f_y = first_parent_pivot
#     x_possibility = [f_x, f_x +1, f_x -1, f_x +2, f_x-2]
#     y_possibility = [f_y, f_y +1, f_y -1, f_y +2, f_y-2]
#     shuffle(x_possibility)
#     shuffle(y_possibility)
#     for new_x in x_possibility:
#         for new_y in y_possibility:
#             if self.id_matrix[new_y][new_x] == 0:
#                 space_size = 1
#                 x_opt = [-1, 0, 1]
#                 y_opt = [-1, 0, 1]
#                 for n_x in x_opt:
#                     for n_y in y_opt:
#                         if space_size < size and n_x != n_y and n_x !=0:
#                             if self.id_matrix[n_y][n_x] == 0:
#                                 new_free_space.append((n_x, n_y))
#                                 space_size +=1
#                 new_free_space.append((new_x, new_y))
#     return new_free_space
