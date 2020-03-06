# try:
# except:
# else:
# finally:


while True:
    try:
        num = int(input("please enter a number: "))
    except ValueError:
        print("That's not a number")
    else:
        print("Good job, you entered a number!")
        break
    finally:
        print("RUNS NO MATTER WAHT")
print("REST OF GAME LOGIC RUNS!")

# try:
#     num = int(input("please enter a number: "))
# except:
#     print("That's not a number")
# else:
#     print("I'm in else")
# finally:
#     print("RUNS NO MATTER WAHT")