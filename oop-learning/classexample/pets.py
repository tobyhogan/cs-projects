"""
name: string
species: string
description: string

"""

class Pet():
    def __init__(self, name, species, description):
        self.name = name
        self.species = species
        self.description = description

    def get_name(self):
        print(self.name)

    def get_species(self):
        print(self.species)
    
    def get_description(self):
        print(self.description)

    def set_name(self, new_name):
        self.name = new_name

    def set_species(self, new_species):
        self.species = new_species

    def set_description(self, new_description):
        self.description = new_description

    def describe(self):
        print(f"Your pet's name is a {self.name}")
        print(f"Your pet is a {self.species}")
        print(f"Your pet's description is: {self.description}")
