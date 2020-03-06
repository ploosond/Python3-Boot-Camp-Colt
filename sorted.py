# users = [
#     {"username": "samuel", "tweets": ["I love cake", "I love pie"]},
#     {"username": "katie", "tweets": ["I love my cat"]},
#     {"username": "jeff", "tweets": [], "color": "purple"},
#     {"username": "bob123", "tweets": [], "num": 10, "color": "teal"},
#     {"username": "doggo_luvr", "tweets": ["dogs are the best", "I'm hungry"]},
#     {"username": "guitar_gal", "tweets": []}
# ]

# sorted(users,key=lambda user: user['username'])
# sorted(users,key=lambda user: len(user['tweets']))

songs = [
    {"title": "happy birthday", "playcount": 1},
    {"title": "Survive", "playcount": 6},
    {"title": "YMCA", "playcount": 99},
    {"title": "Toxic", "playcount": 31}
]

print(min(songs, key=lambda s: s['playcount'])['title'])
# print(sorted(songs, key= lambda s: s['playcount'], reverse=True))


# names = ['Arya', 'Samson', 'Dora','Tim', 'Ollivander']

# # print(min(len(name) for name in names))
# print(max(names, key=lambda n:len(n)))
# print(min(names, key=lambda n:len(n)))