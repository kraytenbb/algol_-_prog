import random
import math
import unittest


def y1(x):
    return math.sin(x)


def y2(x):
    return math.cos(0.5 * x)


def y3(x):
    return math.sin(0.5 * x) - 0.5


def monte_carlo_area(a=6, b=8, num_points=2000000):
    y_min = min(y1(a), y2(a), y3(a), y1(b), y2(b), y3(b))
    y_max = max(y1(a), y2(a), y3(a), y1(b), y2(b), y3(b))
    inside_points = 0
    for _ in range(num_points):
        x = random.uniform(a, b)
        y = random.uniform(y_min, y_max)
        upper = max(y1(x), y2(x), y3(x))
        lower = min(y1(x), y2(x), y3(x))
        if lower <= y <= upper:
            inside_points += 1
    area = (b - a) * (y_max - y_min)
    total_area = (inside_points / num_points) * area
    return total_area


total_area = monte_carlo_area(6, 8, num_points=2000000)
print(f"Оцененная площадь фигуры: {total_area}")


class TestMonteCarloArea(unittest.TestCase):
    def test_area_stability(self):
        result1 = monte_carlo_area(num_points=1000000)
        result2 = monte_carlo_area(num_points=1100000)
        result3 = monte_carlo_area(num_points=1200000)
        self.assertAlmostEqual(result1, result2, places=2)
        self.assertAlmostEqual(result2, result3, places=2)
        self.assertAlmostEqual(result1, result3, places=2)
if __name__ == "__main__":
    unittest.main()
