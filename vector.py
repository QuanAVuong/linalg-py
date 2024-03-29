from math import sqrt, acos, pi

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
    return Vector([ s + v for s, v in zip(self.coordinates, v.coordinates) ])
  
  def minus(self, v):
    return Vector([ s - v for s, v in zip(self.coordinates, v.coordinates) ])
  
  def multiply_scalar(self, c):
    return Vector([ s * c for s in self.coordinates ])

  def magnitude(self):
    return sqrt(sum([ s ** 2 for s in self.coordinates ]))

  def normalize(self):
    try:
      return self.multiply_scalar( 1 / self.magnitude() )
    except ZeroDivisionError:
      raise Exception("Zero vector cannot be normalized")

  def dot(self, v):
    return sum([ s * v for s, v in zip( self.coordinates, v.coordinates ) ])

  def angle(self, v, in_degrees=False):
    try:
      u1 = self.normalize()
      u2 = v.normalize()
      radians = acos(u1.dot(u2))

      if in_degrees:
        return radians * (180 / pi)
      else:
        return radians
    
    except Exception as e:
      # if str(e) == self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG:
      if str(e) == "math domain error":
        raise Exception("Cannot compute an angle with a zero vector")
      else:
        raise e

vector1 = Vector([1, 4, -1])
print(repr(vector1))
print(vector1)

vector2 = Vector([0, 2, 5])
print(repr(vector2))
print(vector2)

vector3 = Vector([1, 4, -1])
print(repr(vector3))
print(vector3)

vector0 = Vector([0, 0, 0])
print(repr(vector0))
print(vector0)

print(vector1 == vector2)
print(vector1 == vector3)

print(f"{vector1} plus\n{vector2} =\n{vector1.plus(vector2)} ")
print(f"{vector2} minus\n{vector3} =\n{vector2.minus(vector3)} ")
print(f"{vector3} scalar multiply {5} =\n{vector3.multiply_scalar(5)}")
print(f"{vector2} magnitude = {vector2.magnitude()} ")
print(f"{vector2} normalized ie. unit vector =\n{vector2.normalize()}")
# print(f"{vector0} normalized ie. unit vector =\n{vector0.normalize()}")
print(f"{vector1} dot product\n{vector2} = {vector1.dot(vector2)} ")
print(f"{vector1} dot product\n{vector3} = {vector1.dot(vector3)} ")

print(f"Angle bewtween {vector1} and {vector2} \n = {vector1.angle(vector2)} radians")
print(f"Angle bewtween {vector1} and {vector2} \n = {vector1.angle(vector2, True)} degrees")
# print(f"Angle bewtween {vector1} and {vector3} \n = {vector1.angle(vector3)} ")
