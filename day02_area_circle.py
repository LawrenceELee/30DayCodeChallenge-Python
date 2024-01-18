import math

def calc_area_circle(radius):

  try:
    radius = float(radius)
  except ValueError:
    raise ValueError("radius must be a number")

  # mathematically, radius cannot be negative
  # a negative circle area doesn't make sense
  if radius < 0:
    raise ValueError("radius cannot be negative")

  return (math.pi) * radius**2

r = input("enter raidus: ")
a = calc_area_circle(r)
print(f"circle with radius {r} has area {a}")
