#Python program to calculate the area of triangle, rectangle and circle
#Area of triangle
a=float(input("Enter the base"))
b=float(input("Enter the height"))
Area=0.5*a*b
print("The area of the triangle is %0.2f" %Area)

#Area of rectangle
a=float(input("Enter the length"))
b=float(input("Enter the breadth"))
Area=(a*b)
print("The area of the rectangle is %0.2f" %Area)

#Area of circle
r=float(input("Enter the radius"))
Area=3.14*r*r
print("The area of the circle is %0.2f" %Area)