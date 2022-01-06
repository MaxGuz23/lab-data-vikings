# Soldier
import random
class Soldier:
    def __init__(self, health, strength):
        # add code here
        self.health = health
        self.strength = strength
    def attack(self):
        return self.strength

    def receive_damage(self, damage):
        if damage == None:
            damage = 0
        self.health -= damage
        return self.health
        

# Viking


class Viking(Soldier):
    def __init__(self, name, health, strength):
        self.name = name
        super().__init__(health,strength)

    def receive_damage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"

    def battle_cry(self):
        return f"Odin Owns You All!"


# Saxon

class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)

    def receive_damage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return f"A Saxon has died in combat"

# War

class War():
    def __init__(self):
        self.viking_army = []
        self.saxon_army = []

    def add_viking(self, Viking):
        self.viking_army.append(Viking)
    def add_saxon(self, Saxon):
        self.saxon_army.append(Saxon)

    def viking_attack(self):
        saxon = random.choice(self.saxon_army)
        viking = random.choice(self.viking_army)
        saxon.receive_damage(viking.attack())

    def saxon_attack(self):
        saxon = random.choice(self.saxon_army)
        viking = random.choice(self.viking_army)
        viking.receive_damage(saxon.attack())

    def show_status(self):
        pass


'''
Returns the current status of the War based on the size of the armies.

should be a function
should receive 0 arguments
if the Saxon list is empty, should return "Vikings have won the war of the century!"
if the Viking list is empty, should return "Saxons have fought for their lives and 
survive another day..."
if there are at least 1 Viking and 1 Saxon, should return "Vikings and Saxons are 
still in the thick of battle."
'''