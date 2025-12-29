a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

# Swapping
a, b, c = b, c, a

print("After swapping:")
print("a =", a)
print("b =", b)
print("c =", c)

#method 2
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z= int(input("Enter third number: "))
temp=0

# Swapping
temp = x
x = y
y = z
z = temp


print("After swapping:")
print("x =", x)
print("y =", y)
print("z =", z)