from math import atan
from math import degrees

ab = int(input())
bc = int(input())

print(round(degrees(atan((ab / 2) / (bc / 2)))))