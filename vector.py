class Vector(object):
  def __init__(self, coordinates):
    try:
      if not coordinates:
        raise ValueError
      self.coordinates = tuple(coordinates)
      self.dimension = len(coordinates)
    
    except ValueError:
      raise ValueError("The coordinates must be nonempty")
    
    except TypeError:
      raise TypeError("The coordinates must be an iterable")

  def __repr__(self):
    return f"<Vector instance - Coordinates: {self.coordinates}. Dimension: {self.dimension}>"

  def __str__(self):
    return f"Vector: {self.coordinates}"

  def __eq__(self, v):
    return self.coordinates == v.coordinates

  def plus(self, v):
    return Vector([ x + y for x, y in zip(self.coordinates, v.coordinates) ])
  
  def minus(self, v):
    return Vector([ x - y for x, y in zip(self.coordinates, v.coordinates) ])
  
  def multiply_scalar(self, c):
    return Vector([ x * c for x in self.coordinates ])

  def magnitude(self):
    from math import sqrt
    return sqrt(sum([ x ** 2 for x in self.coordinates ]))

  def normalize(self):
    try:
      return self.multiply_scalar( 1. / self.magnitude )
    except ZeroDivisionError:
      raise Exception("Zero vector cannot be normalized")

vector1 = Vector([1, 4, -1])
print(repr(vector1))
print(vector1)

vector2 = Vector([0, 2, 5])
print(repr(vector2))
print(vector2)

vector3 = Vector([1, 4, -1])
print(repr(vector2))
print(vector2)

print(vector1 == vector2)
print(vector1 == vector3)

print(f"{vector1} plus\n{vector2} =\n{vector1.plus(vector2)} ")
print(f"{vector2} minus\n{vector3} =\n{vector2.minus(vector3)} ")
print(f"{vector3} scalar multiply {5} =\n{vector3.multiply_scalar(5)}")
print(f"{vector2} magnitude = {vector2.magnitude()} ")
print(f"{vector2} normalized ie. unit vector = {vector2.normalize()}")
