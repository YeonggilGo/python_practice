# https://leetcode.com/problems/spiral-matrix-ii/

from typing import List


class Spiral:
    n: int
    x_dir: int
    y_dir: int
    x_pos: int
    y_pos: int
    result: List[List[int]]

    def __init__(self, n=0):
        self.x_pos, self.y_pos = 0, 0
        self.x_dir, self.y_dir = 1, 0
        self.n = n
        self.result = []
        for i in range(self.n):
            self.result.append([0] * self.n)

    def update_dir(self) -> None:
        if self.x_dir == 1 and self.y_dir == 0:
            self.x_dir, self.y_dir = 0, 1
        elif self.x_dir == 0 and self.y_dir == 1:
            self.x_dir, self.y_dir = -1, 0
        elif self.x_dir == -1 and self.y_dir == 0:
            self.x_dir, self.y_dir = 0, -1
        elif self.x_dir == 0 and self.y_dir == -1:
            self.x_dir, self.y_dir = 1, 0

    def hit_wall(self) -> bool:
        nx, ny = self.x_pos + self.x_dir, self.y_pos + self.y_dir
        cond = nx >= self.n or ny >= self.n or nx < 0 or ny < 0
        return cond or self.result[ny][nx] != 0

    def update_pos(self) -> (int, int):
        if self.hit_wall():
            self.update_dir()
        self.x_pos, self.y_pos = self.x_pos + self.x_dir, self.y_pos + self.y_dir

    def fill_matrix(self) -> List[List[int]]:
        for i in range(1, self.n ** 2 + 1):
            self.result[self.y_pos][self.x_pos] = i
            self.update_pos()
        return self.result


class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        spiral = Spiral(n=n)
        result = spiral.fill_matrix()
        return result
