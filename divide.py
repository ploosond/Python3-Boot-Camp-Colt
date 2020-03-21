# def divide(num_1, num_2):
#     return num_2 // num_1

# print(divide(2,6))
# print(divide(6,12))

# def yell(char):
#     return ("{}!".format(char.upper()))
# print(yell("Prajwol"))

# def sum_odd_numbers(numbers):
#     total = 0
#     for num in numbers:
#         if num % 2 != 0:
#             total += num
#     return total

# print(sum_odd_numbers([1,2,3,4,5,6,7]))

def is_odd_number(num):
    if num % 2 != 0:
        return True
    return False

print(is_odd_number(4)) 