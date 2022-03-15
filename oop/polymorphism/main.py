class Bird:
    def __init__(self, color, name):
        self.color = color
        self.name = name
        self.sound = "Chirp"

    
    def make_sound(self):
        print(self.sound)

    

class Swallow(Bird):
    def __init__(self, color, name):
        super.__init__(color, name)

    
    def make_sound(self):
        print()