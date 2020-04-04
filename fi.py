# def fib_list(max):
#     nums = []
#     a, b = 0, 1
#     while len(nums) < max:
#         nums.append(b)
#         a, b = b, a+b
#     return nums
# # fib_list(1000000)
# def fib_gen(max):
#     x = 0
#     y = 1
#     count = 0
#     while count < max:
#         x, y = y , x + y
#         yield x
#         count += 1

# for n in fib_gen(10):
#     print(n)
def get_multiples(num =1):
    next_num = num
    while True:
        yield next_num
        next_num += num