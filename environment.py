class Entity:
    def __init__(self, hp, defense=False):
        self.hp = hp
        self.defense = defense # 'def' is either True or False
        self.done = False
        self.death = False

    # Basic Functions
    def damage(self, amount):
        self.hp -= amount

    def check_dead(self):
        if self.hp <= 0:
            self.death = True

    def mode_change(self):
        if self.defense == True:
            self.defense = False
        else:
            self.defense = True

    def start_turn(self):
        self.done = False
        #self.defense = False

    def end_turn(self):
        self.done = True

    # Successor Functions
    # Assumes that the arguments are of the Entity() class
    def attack(self, opponent):
        if opponent.defense != True:
            opponent.damage(1)
            opponent.defense = True
        else:
            self.damage(1)

    def defend(self, opponent):
        opponent.defense = False

class State:
    def __init__(self):
        # Initialize initial state
        self.connor = Entity(1)
        self.terminator = Entity(2)
        self.functions = ['attack', 'defend']

    def agent_action(self, action):
        if action == 'attack':
            self.connor.attack(self.terminator)
        else:
            self.connor.defend(self.terminator)
