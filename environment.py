class Entity:
    def __init__(self, hp, defense=False):
        # HP is the hit points
        # Defense is if an Entity is defending
        # Done is a filler attribute for previous purposes, has no point currently
        # Death is checked to check the goal state, has no real point because HP <= 0 can just be done directly
        self.hp = hp
        self.defense = defense # 'def' is either True or False
        self.done = False
        self.death = False

    # Basic Functions
    # Functions to make things work that's not necessarilly related to the AI
    def damage(self, amount):
        # Receive damage or decrement the HP
        self.hp -= amount

    def check_dead(self):
        # Check if HP <= 0, no point tbh
        if self.hp <= 0:
            self.death = True

    def mode_change(self):
        # Filler function, def attack() already does this
        # mode_change complicates things
        if self.defense == True:
            self.defense = False
        else:
            self.defense = True

    def start_turn(self):
        # Filler function for the purposes of previous versions
        self.done = False

    def end_turn(self):
        # Filler function for the purposes of previous versions
        self.done = True

    # Successor Functions
    # Assumes that the arguments are of the Entity() class
    def attack(self, opponent):
        # If attacking Terminator
        # If Terminator defense is not True, damage it then set to True
        # Otherwise, Connor damages himself (Terminator attacks Connor)
        # (AI is not Adversarial AI)
        if opponent.defense != True:
            opponent.damage(1)
            opponent.defense = True
        else:
            self.damage(1)

    def defend(self, opponent):
        # If Connor defends, set Terminator's defense to False
        opponent.defense = False

class State:
    def __init__(self):
        # Initialize initial state
        self.connor = Entity(1)
        self.terminator = Entity(2)

        # Initialize the functions, important for the successor_function function for the AI
        self.functions = ['attack', 'defend']

    def agent_action(self, action):
        # Filler function for the purposes of previous versions
        if action == 'attack':
            self.connor.attack(self.terminator)
        else:
            self.connor.defend(self.terminator)
