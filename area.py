#area of triangle
p=float(input("p: "))
q=float(input("q: "))
r=float(input("r: "))
s=(p+q+r)/2
area=(s*(s-p)*(s-q)*(s-r))
per=p+q+r
print("area of triangle is", area)
print("per is", per)

#area of circle
r=float(input("radius: "))
area=3.14*r*r
print("area of circle is", area)

#area of square
side=float(input("side of square: "))
area=side*side
perimeter=4*side
print("area of square is", area)
print( "perimeter is", perimeter)
