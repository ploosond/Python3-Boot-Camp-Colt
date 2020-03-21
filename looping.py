# numbers = [1, 2, 3, 4, 5]
# doubled_numbers = []

# for num in numbers:
#     doubled_number = num * 2
#     doubled_numbers.append(doubled_number)

# print(doubled_numbers)


# numbers = [1, 2, 3, 4, 5]

# doubled_numbers = [num * 2 for num in numbers]

# print(doubled_numbers)

# names = ['prajwol', 'devkota', 'male','x']

# re_define = [name + ' : correct' for name in names]

# print(re_define)

# name = 'colt'

# rename = [char.upper() for char in name]

# print(rename)

# friends = ['ashley', 'matt', 'michael']

# upper = [friend.upper() for friend in friends]

# print(upper)

# numbers = [1, 2, 3, 4, 5]
# new_list = []
# for num in numbers:
#     convert_to_string = str(num)
#     new_list.append(num)
# print(new_list)

answer = [val for val in [1,2,3,4] if val in [3,4,5,6]]
print(answer)
answer2 = [val[::-1].lower() for val in ["Ellie", "Tim", "Matt"]]
print(answer2)