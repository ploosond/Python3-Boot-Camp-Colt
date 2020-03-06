# while True:
#     command = input("Type 'exit' to quit: \n")
#     if command == 'exit':
#         break

# for x in range(100):
#     print(x)
#     if x == 3:
#         break

times = int(input("How many times do I have to tell you? \n"))

for time in range(times):
    print("CLEAN UP YOUR ROOM!")
    if time >= 4:
        print("do you even listen anymore?")
        break