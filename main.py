import itertools
from typing import List


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.taken = False

    def __repr__(self):
        return f"x:{self.x}|y:{self.y}"

    def slope(self, other):
        if other.x == self.x:
            return 0
        return (other.y - self.y) / (other.x - self.x)

    def is_collinear(self, other):
        return self.slope(other) == 1

    def mark_taken(self):
        self.taken = True

    def is_taken(self):
        return self.taken

class Manager:
    def __init__(self, points: List[list]):
        self.comb_points: list = points
        self.lines: list = []
        self.count: int = 0

    def collinear(self, p1: Point, p2: Point, p3: Point) -> bool:
        is_p1p2_collinear = p1.slope(p2)
        is_p2p3_collinear = p2.slope(p3)
        return is_p1p2_collinear == is_p2p3_collinear

    def process(self):  # need a better name for this
        for each_pair in self.comb_points:
            p1, p2, p3 = each_pair
            if p1.is_taken() or p2.is_taken() or p3.is_taken():
                continue
            if self.collinear(p1, p2, p3):
                p1.mark_taken()
                p2.mark_taken()
                p3.mark_taken()
                self.lines.append(each_pair)
                self.count += 1

    def get_count(self):
        return self.count
    def get_lines(self):
        return self.lines


if __name__ == '__main__':
    # points = [Point(1, 1),
    #           Point(1, 2),
    #           Point(1, 3)]

    # points = [Point(1, 1),
    #           Point(2, 2),
    #           Point(3, 3),
    #           Point(4, 4)
    #           Point(5, 5)
    #           Point(6, 6)]

    # points = [Point(10, 1),
    #           Point(10, 2),
    #           Point(10, 3),
    #           Point(11, 4),
    #           Point(11, 5),
    #           Point(11, 6)]

    # points = [Point(7, 1),
    #           Point(7, 2),
    #           Point(8, 3),
    #           Point(8, 4),
    #           Point(9, 5),
    #           Point(9, 6)]

    points = [Point(1, 1),
              Point(2, 2),
              Point(3, 3),
              Point(4, 4),
              Point(5, 5),
              Point(6, 6),
              Point(7, 1),
              Point(7, 2),
              Point(8, 3),
              Point(8, 4),
              Point(9, 5),
              Point(9, 6),
              Point(10, 1),
              Point(10, 2),
              Point(10, 3),
              Point(11, 4),
              Point(11, 5),
              Point(11, 6)]

    comb_points = list(itertools.combinations(points, 3))
    manager = Manager(list(comb_points))
    manager.process()

    assert 1 == manager.get_count()
