# for num in range(1,21):
#     if num == 4 or num == 13:
#         print(f"{num} is UNLUCKY!")
#     elif num % 2 != 0:
#          print(f"{num} is odd")
#     else:
#         print(f"{num} is even")


for num in range(1,21):
    if num == 4 or num == 13:
        state = "UNLUCKY"
        # print(f"{num} is {state}")
    elif num % 2 != 0:
        state = "odd"
        # print(f"{num} is {state}")
    else:
        state = "even "
    print(f"{num} is {state}")