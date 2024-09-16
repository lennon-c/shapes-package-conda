class Rectangle:
  def __init__(self, w, h):
    self.width = w
    self.height = h

  def area(self):
    return self.width * self.height

  def perimeter(self):
    return (2 * self.width) + (2 * self.height)

if __name__ == '__main__':
  r = Rectangle(5, 10)
  print(f'area: {r.area()}')
  print(f'perimeter: {r.perimeter()}')