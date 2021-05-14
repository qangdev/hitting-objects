import pytest
from main import Manager, Point


def test_simple_line():
    points = [Point(1, 1),
              Point(2, 2),
              Point(3, 3)]
    manager = Manager(points)
    manager.process()
    assert 1 == manager.count_line()


def test_first_line():
    points = [Point(1, 1),
              Point(2, 2),
              Point(3, 3),
              Point(4, 4),
              Point(5, 5),
              Point(6, 6)]
    manager = Manager(points)
    manager.process()
    assert 1 == manager.count_line()


def test_2nd_3rd_lines():
    points = [Point(7, 1),
              Point(7, 2),
              Point(8, 3),
              Point(8, 4),
              Point(9, 5),
              Point(9, 6)]
    manager = Manager(points)
    manager.process()
    assert 2 == manager.count_line()


def test_4th_5th_lines():
    points = [Point(10, 1),
              Point(10, 2),
              Point(10, 3),
              Point(11, 4),
              Point(11, 5),
              Point(11, 6)]
    manager = Manager(points)
    manager.process()
    assert 2 == manager.count_line()


def test_merge_lines():
    points = [Point(7, 1),
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
    manager = Manager(points)
    manager.process()
    assert 4 == manager.count_line()


def test_least_lines():
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
    manager = Manager(points)
    manager.process()
    assert 5 == manager.count_line()
