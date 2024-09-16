class Square:
  def __init__(self, s):
    self.side = s

  def area(self):
    return self.side ** 2

  def perimeter(self):
    return 4 * self.side

if __name__ == '__main__':
  s = Square(5)
  print(f'area: {s.area()}')
  print(f'perimeter: {s.perimeter()}')