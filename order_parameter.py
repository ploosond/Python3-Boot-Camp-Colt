# def display_info(a, b, *args, instructor="Colt", **kwargs):
#     return [a, b, args, instructor, kwargs]

# print(display_info(1, 2, 3, last_name="Steele", job="Instructor"))

# def sum_all_values(*args):
#     print(args)
#     total = 0
#     for num in args:
#         total += num
#     print(total)

# # sum_all_values(1,2,3,4,5,)
# # sum_all_values(5,6)
# nums =[1,2,3,4,5,6]
# sum_all_values(*nums)

# def display_names(first, second):
#     print(f"{first} says hello to {second}")
# names = {"first": "Colt", "second": "Rusty"}
# # display_names(first= "Charile", second= "Sue!")
# # display_names(names)
# display_names(**names)

def add_and_multiply_numbers(a,b,c,**kwargs):
    print(a + b * c)
    print("OTHER STUFF....")
    print(kwargs)

data = dict(a=1,b=2,c=3,d=55,name="Tony")

# add_and_multiply_numbers(data)
print(add_and_multiply_numbers(**data, cat="blue"))
