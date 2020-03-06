# playlist = {
#     'title': 'patagonia bus', 
#     'author': 'colt steele', 
#     'songs': [
#         {'title': 'song1', 'artist': ['blue'], 'duration': 2.5}, 
#         {'title': 'song2', 'artist': ['kitty', 'djcat'], 'duration': 5.25}, 
#         {'title': 'meowmeow', 'artist': ['garfield'], 'duration': 2.0}
#     ]
# }
# total_length = 0
# for song in playlist['songs']:
#     total_length += song['duration']
# print(total_length)

# numbers = {'first': 1, 'second': 2, 'third': 3}
# squared_numbers = {key:value ** 2 for key,value in numbers.items()}
# print(squared_numbers)

# numbers2 = {num: num ** 2 for num in [1,2,3,4,5]}
# print(numbers2)

# str1 = "ABC"
# str2 = "123"
# combo = {str1[i]:str2[i] for i in range(0,len(str1))}
# print(combo)

# instructor = {'name': 'colt', 'city': 'san francisco', 'color': 'purple'}
# yelling_instructor = {k.upper():v.upper() for k,v in instructor.items()}
# print(yelling_instructor)

# students = ["Prajwol", "Roshan", "Dhurba", "Suman", "Dipendra"]
# student_dict = {student:f"Mr.{student}" for student in students}
# print(student_dict)

# dict_multi = {num: num ** 2 for num in range(1,50)}
# print(dict_multi)