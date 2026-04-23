#tehtävä 4

import math

def create_point (x, y):
    return (x, y)

def distance (p1, p2):
    x1, x2 = p1
    y1, y2 = p2
    d = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return d

x1 = float(input("Anna x1: "))
y1 = float(input("Anna y1: "))
x2 = float(input("Anna x2: "))
y2 = float(input("Anna y2: "))

p1 = create_point(x1, y1)
p2 = create_point(x2, y2)

d = distance(p1, p2)

print(f"Etäisyys: {d:.2f} ")
