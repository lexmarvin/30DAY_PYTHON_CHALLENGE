import math

# arithmetic challenges

#Calculate the area of a circle given a radius (you choose the number).

radius = float(input("Enter the radius of the circle: "))

areaOfCircle = math.pi * radius ** 2
print(f"the area of a circle is:{areaOfCircle:.2f}")


#Convert Celsius to Fahrenheit (and vice versa).

fahr = float(input("Enter temperature in Fahrenheit: "))

celsius = (fahr - 32) * 5/9
print(f"the converted celsius is:{celsius:.2f}")


# Write a small calculator that takes two numbers and prints out their sum, difference, product, and quotient.

value1 = float(input("Enter value 1: "))
value2 = float(input("Enter value 2: "))

value1 = float(input("Enter value 1: "))
value2 = float(input("Enter value 2: "))

print("Choose 1 operator (Addition, Subtraction, Multiplication, Division)")

operation = input("What operation do you want to do: ")

if operation == "Addition":
    print(f"The sum is: {value1 + value2}")   

elif operation == "Subtraction":
    print(f"The difference is: {value1 - value2}")   

elif operation == "Multiplication":
    print(f"The product is: {value1 * value2}")   

elif operation == "Division":
    print(f"The quotient is: {value1 / value2}")   

else:
    print("mali ka.")

print (f"The sum is: {sum:.2f}")
print (f"The difference is: {difference:.2f}")
print (f"The product is: {product:.2f}")
print (f"The quotient is: {quotient:.2f}")
sum = (value1 + value2)
difference =  (value1 - value2)
product =  (value1 * value2)
quotient =  (value1 / value2)


# Find the remainder when dividing 25 by 4, then explain what the modulus operator is doing.

remainder = 25 % 4
print(f"The remainder is: {remainder}")

# The modulus operator (%) returns the remainder of a division operation.
# In this case, 25 divided by 4 is 6 with a remainder of 1, so the modulus operator gives us 1.

