#4.Write a script a script that prompts user to enter base and height of triangle
# and calculate the area of this triangle (area = 0.5 * b * h)

base = int(input('Enter base: '))
height = int(input('Enter height: '))
area = (0.5 * float(base) * float(height))

print('The area of the triangle is',int(area))

#5.Write a script that prompts the user to to enter side a,b and c
# and calculate the perimeter of the triangle (perimeter = a + b + c)

a = int(input('Enter side a: '))
b = int(input('Enter side b: '))
c = int(input('Enter side c: '))
perimeter = float(a) + float(b) + float(c)

print('The perimeter of the triangle is',int(perimeter))

