# def sum_all_nums(*args):
#     total = 0
#     for num in args:
#         total += num
#     return total

# print(sum_all_nums(1,2,3,4,5,6,7,8,9))
# print(sum_all_nums(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)) 

def ensure_correct_info(*args):
    if "Prajwol" in args and "Devkota" in args:
        return "Welcome back Prajwol Devkota"
    return "Not sure who are you........."

print(ensure_correct_info(True, False, "Prajwol", "Devkota"))
print(ensure_correct_info(True, False, "Prajwol", "Dalls"))