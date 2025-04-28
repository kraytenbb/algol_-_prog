import random
import math

def y1(x):
    return math.sin(x)

def y2(x):
    return math.cos(0.5 * x)

def y3(x):
    return math.sin(0.5 * x) - 0.5
num_points=int(input("Введите N: "))
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
