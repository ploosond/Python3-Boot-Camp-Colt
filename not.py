age = 78
# 2-8 2 dollars ticket
# 65 5 dollars ticket
# 10 dollars for everyone else

if not ((age >= 2 and age <= 8) or age >=65):
    print('You pay 10 dollars and are not a child or senior citizen!')
else: print('You are a child or senior')