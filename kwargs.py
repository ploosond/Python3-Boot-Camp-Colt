# def fav_colors(**kwargs):
#     for person, color in kwargs.items():
#         print(f"{person}'s favorite color is {color}")

# fav_colors(colt="purple", ruby="red", ethel="teal")
# fav_colors(colt="royal deep amazing purple")

# def special_greeting(**kwargs):
#     if "David" in kwargs and kwargs["David"] == "special":
#         return "You get a special greeting David"
#     elif "David" in kwargs:
#         return f"{kwargs['David']} David!"
#     return "Not sure who this is .........."

# print(special_greeting(David="Hello"))
# print(special_greeting(Bob="hello"))
# print(special_greeting(David="special"))
# print(special_greeting(Heather="Hello", David="special"))

# def combine_words(word, **kwargs):
#     if 'prefix' in kwargs:
#         return kwargs['prefix'] + word
#     elif 'suffix' in kwargs:
#         return word + kwargs['suffix']
#     return word
    
# print(combine_words('Mr.',prefix= "Prajwol", suffix="Devkota"))