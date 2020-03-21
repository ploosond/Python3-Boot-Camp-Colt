# coords = [[10.423, 9.132], [37.212, -14.092], [21.367, 32.572]]

# for loc in coords:
#     for coord in loc:
#         print(coord)

# nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# [[print(val) for val in l] for l in nested_list]

# board = [[num for num in range(1, 4)] for val in range(1, 4)]
# print(board)

# x_o = [["X" if num % 2 != 0 else "O" for num in range(1, 4)] for val in range(1, 4)]
# print(x_o)

# x_o2 = [["*" for x in range(1, 4)] for i in range(5, 8)]
# print(x_o2)

# new_list = [[i for i in range(1,3)] for num in range(1,4)]
# print(new_list)

# answer = [[x for x in range(0, 10)]for num in range(0, 10)]
# print(answer)

# instructor = {"name": "Prajwol", "owns_dog": True, "num_courses": 1, "favorite_language": "Python", "is_hilarious": False, 7: "my ffavorite number!"}
# print(instructor)

# instructor = {"name": "Colt", "owns_dog": True, "num_courses": 1, "favorite_language": "Python", "is_hilarious": False, 7: "my favorite number"}
# for k, v in instructor.items():
#     print(f"key is {k} and value is {v}")

first = dict(a=1,b=2,c=3,d=4,e=5)
second = {}
second.update(first)
print(second)

second['a'] = "AMAZING"
print(second)
second.update(first)

print(second)