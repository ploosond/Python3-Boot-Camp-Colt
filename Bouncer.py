# # ask for age
# print('How old are you?')
# age = input()
# if age:
#     age = int(age)
#     if age >= 18 and age < 21:
#         # 18-21 wristband
#         print('You can enter, but need a wristband!')
#     elif age >= 21:
#         # 21+ drink, normal entry
#         print('You are good to enter and can drink!')
#     else:
#         # too young, sorry
#         print('You can\'t come in, little one :(!')
# else:
#     print('Please enter your age')

print('How old are you?')
age = input()
if age:
    age = int(age)
    if age >= 21:
        print('You are good to enter and can drink!')
    elif age >= 18:
        # 21+ drink, normal entry
        print('You can enter, but need a wristband!')
    else:
        # too young, sorry
        print('You can\'t come in, little one :(!')
else:
    print('Please enter your age')    