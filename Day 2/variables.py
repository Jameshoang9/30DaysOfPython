#Day 2:30 Days of python programming'
#exercise 1: Assigning variables
import math

first_name = 'James'
last_name = 'Hoang'
full_name = 'James Hoang'
country = 'United Kingdom'
City = 'London'
age = '22'
year = '1999'
is_married = 'no'
first_name, last_name, full_name, country, city = 'James', 'Hoang', 'James Hoang', 'United Kingdom', 'London'

#exercise 2
print(type(first_name))
print(len(first_name))
print(len(first_name)==len(last_name)) #true because same length
print(len(first_name)==len(country)) #false because different length

#manipulating numbers using variables
num_one = 5
num_two = 4

total = num_one+num_two
print(total)

diff = num_one-num_two
print(diff)

product = num_one*num_two
print(product)

division = num_one/num_two
print(division)

remainder = num_one%num_two
print(remainder)

exp = num_one**num_two
print(exp)

floor_division = num_one//num_two
print(floor_division)

print(math.pi*30**2)
area_of_circle = math.pi*30**2
print(area_of_circle)

print(2*math.pi*30)
circum_of_circle = 2*math.pi*30
print(circum_of_circle)
#calculating the area of circle by making the radius a user input
radius = input('enter radius')

#how to convert singular string to an integer
print(math.pi*int(radius)**2)
print(type(radius)) #to determine whether it is a str or int

#how to convert whole string to an integer
radius = int(input('enter radius'))
print(math.pi*radius**2)
print(type(radius)) #to determine whether it is a str or int

#using built-in input functions
first_name = input('enter first name')

last_name = input('enter last name')

country = input('enter country')

age = input ('enter age')

print(first_name)
print(last_name)
print(country)
print(age)

#For help
print(help('keywords'))