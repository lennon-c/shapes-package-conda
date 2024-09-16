import math

class Circle:
  def __init__(self, r):
    self.radius = r

  def area(self):
    return math.pi * (self.radius ** 2)

  def circumference(self):
    return 2 * math.pi * self.radius

if __name__ == '__main__':
  c = Circle(10)
  print(f'area: {c.area()}')
  print(f'circumference: {c.circumference()}')