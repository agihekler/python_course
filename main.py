# Assignment 1
# November 11,2020
import trapezoid 
import parallelogram
import circle
import square
import rectangle
import triangle

# main function
def main(): 

  # Circumference and Area of circle
  r = 3
  c = circle.circumference(r)
  a_circle = circle.area(r)
  print ("Circle with r = 3")
  print ("-----------------")
  print ("Circumference is", c)
  print ("Area is", a_circle)

  # Perimeter and Area of square
  l = 2
  p_square = square.perimeter(l)
  a_square = square.area(l)
  print ("")
  print ("Square with l = 2 cm")
  print ("-----------------")
  print ("Perimeter is", p_square, "cm")
  print ("Area is", a_square,"cm squared" )

  #Perimeter and Area of Rectangle 
  w = 4
  p_rectangle = rectangle.perimeter(w,l)
  a_rectangle = rectangle.area(w,l)
  print ("")
  print ("Rectangle with w = 4  and l = 2 cm")
  print ("-----------------")
  print ("Perimeter is", p_rectangle, "cm")
  print ("Area is", a_rectangle, "cm squared")

  #Perimeter and Area of Triangle
  a = 4
  b = 3
  c = 5
  h = 2
  p_triangle = triangle.perimeter(a,b,c)
  a_triangle = triangle.area (b,h)
  print ("")
  print ("Triangle a = 4, b = 3, c = 5 and h = 2 cm")
  print ("-----------------")
  print ("Perimeter is", p_triangle, "cm")
  print ("Area is", a_triangle, "cm squared") 

  #Perimeter and area of Parallelogram
  p_parallelogram = parallelogram.perimeter (a,b)
  a_parallelogram = parallelogram.area (b,h)
  print ("")
  print ("Parallelogram with a = 4, b = 3 and h = 2 cm")
  print ("-----------------")
  print ("Perimeter is", p_parallelogram, "cm")
  print ("Area is", a_parallelogram, "cm squared")

  #Perimeter and area of Trapezoid 
  d = 6
  p_trapezoid = trapezoid.perimeter (a,b,c,d)
  a_trapezoid = trapezoid.area (a, b,h)
  print ("")
  print ("Parallelogram with a= 4, b = 3, c = 5, d = 6 and h = 2 cm")
  print ("-----------------")
  print ("Perimeter is", p_trapezoid, "cm")
  print ("Area is", a_trapezoid, "cm squared")

if __name__ == "__main__":
  main()

