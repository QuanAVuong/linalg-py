class Vector(object):
  def __init__(self, coordinates):
    try:
      if not coordinates:
        raise ValueError
      self.coordinates = tuple(coordinates)
      self.dimension = len(coordinates)