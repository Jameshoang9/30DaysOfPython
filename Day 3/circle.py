import math
#7.Calculate area and circumfrence of circle
# area = pi * r**2
# circumfrence = 2 * pi * r

r = input('Enter radius: ')

area = math.pi * float(r) ** 2
circumfrence = 2 * math.pi * float(r)

print ('The area of the circle is', float(area))
print ('The circumfrence of the circle is', float(circumfrence))

