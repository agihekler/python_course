# Assignment 1
# November 11,2020

# declare variables
def main(): 
  r = 3
if __name__ == "__main__":
  main()
r = 3
import math
c = 2*math.pi*r
a_circle = math.pi*r**2
l = 2
p_square = 4*l/1
a_square = l*l/1
w = 4
p_rectangle = 2*l + 2*w/1
a_rectangle = l*w/1
a_side = 1
b_side = 2
c_side = 3
d_side = 5
height = 3
p_triangle = a_side + b_side + c_side/1
a_triangle = b_side * height/2
p_parallelogram = 2*a_side + 2*b_side/1 
a_parallelogram = b_side * height/1
p_trapezoid = a_side + b_side + c_side + d_side/1
a_trapezoid = a_side + b_side/2*height 

# Circumference and Area of circle
import circle

print ("Circle with r = 3")
print ("-----------------")
print ("Circumference is", c)
print ("Area is", a_circle)

# Perimeter and Area of square
import square 

print ("")
print ("Square with l = 2 cm")
print ("-----------------")
print ("Perimeter is", p_square, "cm")
print ("Area is", a_square,"cm squared" )

#Perimeter and Area of Rectangle 
import rectangle 

print ("")
print ("Rectangle with l = 2 cm and w = 4 cm")
print ("-----------------")
print ("Perimeter is", p_rectangle, "cm")
print ("Area is", a_rectangle,"cm squared" )

#Perimeter and Area of Triangle
import triangle

print ("")
print ("Rectangle with side lengths of 1, 2, 3 cm and a height of 3 cm")
print ("-----------------")
print ("Perimeter is", p_triangle, "cm")
print ("Area is", a_triangle,"cm squared")

#Perimeter and area of Parallelogram 
import parallelogram

print ("")
print ("Parallelogram with side lengths of 1, 2 cm and a height of 3 cm")
print ("-----------------")
print ("Perimeter is", p_parallelogram, "cm")
print ("Area is", a_parallelogram,"cm squared")

#Perimeter and area of Trapezoid 
import trapezoid

print ("")
print ("Trapezoid with side lengths of 1, 2, 3, 5 cm and a height of 3 cm")
print ("-----------------")
print ("Perimeter is", p_trapezoid, "cm")
print ("Area is", a_trapezoid,"cm squared")

