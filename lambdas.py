def square(num): return num * num

square2 = lambda num: num * num

add = lambda a,b: a + b
print(add(3,10))
print(square(9))
print(square(7))

print(square.__name__)
print(square2.__name__)
print(add.__name__)