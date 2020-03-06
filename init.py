class User:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age

user1 = User("Joe", "Smith", 68)
user2 = User("Blanca", "lopez", 41)
print(user1.first, user1.last)
print(user2.first, user2.last)

class Comment:
    def __init__(self, username, text, likes = 0):
        self.username = username
        self.text = text
        self.likes = likes
c = Comment("davey123", "lol you're so silly", 3)
print(c.username, c.text, c.likes)