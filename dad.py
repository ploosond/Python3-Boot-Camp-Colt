import requests
from random import choice
from pyfiglet import figlet_format
from termcolor import colored 

header = figlet_format("DAD JOKE 3000!")
header = colored(header, color="magenta")
print(header)

user_input = input("Ley me tell you a joke! Give me a topic: ")
url = "https://icanhazdadjoke.com/search"
res = requests.get(url,
    headers={"Accept": "application/json"},
    params={"term": user_input}
    ).json()
num_jokes = res["total_jokes"]
results = res["results"]
if num_jokes > 1:
    print(f"I found {num_jokes} jokes about {user_input}. Here' one:")
    print(choice(results)["joke"])
elif num_jokes == 1:
    print(results[0]["joke"])
    print(f"I found one joke about {user_input}:")
else:
    print(f"Sorry, couldn't find a joke with your term: {user_input}")


