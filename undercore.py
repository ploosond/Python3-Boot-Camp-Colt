# __name
# __name
# __name__

class Person:
    def __init__(self):
       self.name = "Tony"
       self._secret = "hi!"
       self.__msg = "I like turtle!"
       self.__lol = "hahahahah"
    # def doorman(self, guess):
    #     if guess == self._secret:
    #         let them in

p = Person()
print(p.name) 
print(dir(p))