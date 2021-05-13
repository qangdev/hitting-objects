from main import Manager, Point

def test_first_line():
    points = [Point(1, 1),
              Point(2, 2),
              Point(3, 3),
              Point(4, 4),
              Point(5, 5),
              Point(6, 6)]
    comb_points = list(itertools.combinations(points, 3))
    manager = Manager(list(comb_points))
    manager.process()
