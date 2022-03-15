class Monster():
    def __init__(self, name: str, hp: int, dialogue: str):
        self.name = name
        self.hp = hp
        self.dialogue = dialogue
        self.attacked = []
        self.damage_done = 0
        self.is_dead = False


    def speak(self):
        print(self.dialogue)


    def take_damage(self, damage: int):
        self.hp -= damage

        if self.hp < 0:
            self.is_dead = True
            self.hp = 0

    
    def attack(self, damage_done: int, attackee):
        self.attacked.append(attackee)
        self.damage_done += damage_done


    def get_name(self):
        print(self.name)


    def set_name(self, name: str):
        self.name = name


    def get_hp(self):
        print(self.hp)


    def set_hp(self, hp):
        self.hp = hp


    def get_dialogue(self):
        print(self.dialogue)


    def set_dialogue(self, dialogue):
        self.dialogue = dialogue

    
    def get_damage_done(self):
        print(self.damage_done)

    
    def set_damage_done(self, damage_done: int):
        self.damage_done = damage_done

    
    def get_attacked(self):
        print(self.attacked.split(", "))

    
    def set_attacked(self, attacked):
        self.attacked = attacked

    
    def get_is_dead(self):
        print(self.is_dead)


    def set_is_dead(self, status):
        self.is_dead = status


        


class Zombie(Monster):
    def __init__(self, name: str, hp: int, dialogue: str):
        super().__init__(name, hp, dialogue)
        self.monster_type = "Zombie"


class Ghost(Monster):
    def __init__(self, name: str, hp: int, dialogue: str):
        super().__init__(name, hp, dialogue)
        self.monster_type = "Ghost"