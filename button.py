# import tkinter as tk
# # DON'T WORRY ABOUT ANY OF THIS CODE
# root = tk.Tk()
# frame = tk.Frame(root)
# frame.pack()


# def say_hi():
#     print("HELLO!")

# button = tk.Button(frame, text="CLICK ME", fg="red", command=say_hi)

# # DON;T WORRY ABOUT THIS CODE
# button.pack(side=tk.LEFT)
# root.mainloop()

# nums = [2,4,6,8,10]
# new_list = []
# for num in nums:
#     double = num * 2
#     new_list.append(double)
# print(new_list)

# people = ["Darcy", "Christian", "Dana", "Annabel"]

# peeps = map(lambda char: char.upper(), people)
# print(list(peeps))
# nums = [2,4,6,8,10]
# doubles = list(map(lambda x : x * 2, nums))
# print(doubles)

final_result = []
def decrement_list(new_list):
    for num in new_list:
        result = num - 1
        final_result.append(result)
    return final_result

print(decrement_list([1,2,3,4]))