import math

def calc_hex_area(base):
  return 3 * math.sqrt(3) * (base ** 2)

def calc_side_area(base, height):
  return base * height * 6

def display_surface_area(base, height):
  print("The total surface area is {:.3f} square feet".format((calc_hex_area(base) + calc_side_area(base, height))), end = "")

height = float(input("Enter height of the base edge in feet : "))
base = float(input("Enter length of hexagonal prism in feet: "))


hex_area = calc_hex_area(base)
print("Surface area of hexagonal faces is {:.3f} square feet".format((hex_area)))

side_area = calc_side_area(base, height)
print("Surface area of rectangular sides is {:.3f} square feet".format((side_area)))

display_surface_area(base,height)
