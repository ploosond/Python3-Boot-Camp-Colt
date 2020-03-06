# class User:
#     def __init__(self, first, last, age):
#         self.first = first
#         self.last = last
#         self.age = age

#     def full_name(self):
#         return f"{self.first} {self.last}"

#     def initials(self, position):
#         return f"{self.first[0]}.{self.last[0]}.{position}"

#     def likes(self, thing):
#         return f"{self.first} likes {thing}"

#     def is_senior(self):
#         return self.age >= 65

#     def birthday(self):
#         self.age += 1
#         return f"Happy {self.age}th, {self.first}"

# user1 = User("Joe", "Smith", 68)
# user2 = User("Blanca", "Lopez", 41)
# print(user1.initials())
# print(user2.initials())
# print(user1.initials("007"))
# print(user1.likes("Ice Cream"))
# print(user2.likes("Chips"))
# print(user1.is_senior())
# print(user2.is_senior())
# print(user1.age)
# print(user1.birthday())
# print(user2.birthday())

class BankAccount:
    def __init__(self, owner, balance = 0.0):
        self.owner = owner
        self.balance = balance

    def is_deposit(self, deposit):
        self.balance += deposit
        return self.balance

    def is_withdraw(self, withdraw):
        self.balance -= withdraw
        return self.balance

ac = BankAccount("Prajwol Devkota")
print(ac.owner, ac.balance)
print(ac.is_deposit(10))
print(ac.is_withdraw(5))
    