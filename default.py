# instructor1 = 'Mary'
# def say_hello():
#     instructor2 = 'Colt'
#     return f'Hello {instructor2}'

# print(say_hello())

# print(instructor1)
# # print(instructor2)

# total = 0

# def increment():
#     global total
#     total += 1
#     return total

# print(increment())

# def outer():
#     count = 0
#     def inner():
#         nonlocal count
#         count += 1
#         return count
#     return inner()

# print(outer())

def say_hello():
    """A simple function that returns the string hello"""
    return "Hello!"
print(say_hello.__doc__)

print([1,2,3].pop.__doc__)