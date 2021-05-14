import itertools
from typing import List


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.taken = False

    def __repr__(self):
        return f"({self.x}:{self.y}"

    def __str__(self):
        return f"{self.x}:{self.y}"

    def slope(self, other):
        if other.x == self.x:
            return 0
        return (other.y - self.y) / (other.x - self.x)

    def mark_taken(self):
        self.taken = True

    def is_taken(self):
        return self.taken


class Line:
    def __init__(self, points: List[Point]):
        self.points = points
        self.taken = False

    def __add__(self, other):
        self.points + other.points

    def __repr__(self):
        return "|".join([str(p) for p in self.points])

    def get_points(self):
        return self.points

    def unpack_points(self):
        return self.points

    def mark_taken(self):
        self.taken = True

    def is_taken(self):
        return self.taken


class Manager:
    def __init__(self, points: List[list]):
        self.points: list = []
        self.pair_points: list = self.generate_pair_points(points)
        self.lines: List[Line] = []

    def generate_pair_points(self, points) -> list:
        return list(itertools.combinations(points, 3))

    def generate_pair_lines(self, lines) -> list:
        return list(itertools.combinations(lines, 2))

    def collinear_points(self, p1: Point, p2: Point, p3: Point) -> bool:
        is_p1p2_collinear = p1.slope(p2)
        is_p2p3_collinear = p2.slope(p3)
        is_p1p3_collinear = p1.slope(p3)
        return is_p1p2_collinear == is_p2p3_collinear == is_p1p3_collinear

    def collinear_lines(self, l1: Line, l2: Line):
        l1p1, l1p2, l1p3 = l1.unpack_points()
        l2p1, l2p2, l2p3 = l2.unpack_points()

        l1p1_l1p2_slope = l1p1.slope(l1p2)
        l1p2_l1p3_slope = l1p2.slope(l1p3)
        l1p3_l2p1_slope = l1p3.slope(l2p1)
        l2p1_l2p2_slope = l2p1.slope(l2p2)
        l2p2_l2p3_slope = l2p2.slope(l2p3)
        l1p1_l2p3_slope = l1p1.slope(l2p3)

        return l1p1_l1p2_slope == l1p2_l1p3_slope == l1p3_l2p1_slope == l2p1_l2p2_slope == l2p2_l2p3_slope == l1p1_l2p3_slope

    # TODO: Refactor this function
    def process(self):  # need a better name for this
        for each_pair in self.pair_points:
            p1, p2, p3 = each_pair
            if p1.is_taken() or p2.is_taken() or p3.is_taken():
                continue
            if self.collinear_points(p1, p2, p3):
                p1.mark_taken()
                p2.mark_taken()
                p3.mark_taken()
                self.lines.append(Line(each_pair))
        if self.lines:
            for pair_line in self.generate_pair_lines(self.lines):
                line_one, line_two = pair_line
                if line_one.is_taken() or line_two.is_taken():
                    continue
                if self.collinear_lines(line_one, line_two):
                    line_one.mark_taken()
                    line_two.mark_taken()
                    self.merge_lines(line_one, line_two)

    def merge_lines(self, line_1, line_2):
        new_line = Line(points=line_1.get_points() + line_2.get_points())
        self.lines.remove(line_1)
        self.lines.remove(line_2)
        self.lines.append(new_line)

    def count_line(self):
        return len(self.lines)

    def get_lines(self):
        return self.lines
