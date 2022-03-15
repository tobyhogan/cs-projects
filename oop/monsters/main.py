from monster import Zombie, Ghost

zombie_leader = Zombie("Whiskey", 175, "I am the leader for the zombies.")
zombie_fighter = Zombie("Alpha", 125, "I am the fighter for the zombies.")

ghost_leader = Ghost("Bravo", 200, "I am the leader for the ghosts.")
ghost_figter = Ghost("Tango", 100, "I am a fighter for the ghosts.")


ghost_leader.speak()
zombie_leader.speak()

for i in range(20):
    zombie_leader.take_damage(10)
    ghost_leader.attack(10, "Whiskey")

zombie_leader.get_is_dead()
zombie_leader.get_hp()
