# class Pet:
#     allowed = ['cat', 'dog', 'fish', 'rat']
#     def __init__(self, name, species):
#         if species not in Pet.allowed:
#             raise ValueError(f"You can't have a {species} pet!")
#         self.name = name
#         self.species = species
#     def set_species(self, species):
#         if species not in Pet.allowed:
#             raise ValueError(f"You can't have a {species} pet!")
#         self.species = species

# cat = Pet("Blue", "cat")
# dog = Pet("Wyatt", "dog")

# print()

class Chicken:
    total_eggs = 0
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.eggs = 0

    def lay_egg(self):
        self.eggs += 1
        Chicken.total_eggs += 1
        return self.eggs

c1 = Chicken("blue", "chicken")
print(Chicken.total_eggs)
print(c1.lay_egg())
print(Chicken.total_eggs)