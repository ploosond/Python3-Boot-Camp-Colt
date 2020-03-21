# names = ['austin', 'penny', 'authony', 'angel', 'billy']
# a_names = filter(lambda name: name[0] == 'a', names)
# print(list(a_names))

users = [
    {"username": "samuel", "tweets": ["I love cake", "I love pie"]},
    {"username": "katie", "tweets": ["I love my cat"]},
    {"username": "jeff", "tweets": []},
    {"username": "bob123", "tweets": []},
    {"username": "doggo_luvr", "tweets": ["dogs are the best", "I'm hungry"]},
    {"username": "guitar_gal", "tweets": []}
]

# inactive_users = list(filter(lambda u: not u['tweets'], users))
# print(inactive_users)
inactive_user2 = [user["username"].upper() for user in users if not user["tweets"]]
print(inactive_user2)
# usernames = list(map(lambda user: user["username"].upper(), 
#     filter(lambda u: not u["tweets"], users)))
# print(usernames)
# names = ['Lassie', 'Colt', 'Rusty']

# result = list(map(lambda char: f"Your instructor is {char}",filter(lambda name: len(name) < 5, names)))

# print(result)