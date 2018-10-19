from environment import State
from utils import Node, Fringe, Queue

def goal_test(state):
    state.connor.check_dead()
    state.terminator.check_dead()
    if state.connor.death == False and state.terminator.death == True:
        return True

def successor_function(state):
    action = state.functions
    result = []
    for x in range(len(action)):
        new_state = State()
        new_state.connor.hp = state.connor.hp
        new_state.terminator.hp = state.terminator.hp
        new_state.terminator.defense = state.terminator.defense
        connor = new_state.connor
        terminator = new_state.terminator

        if action[x] == 'attack':
            connor.attack(terminator)
            result.append(new_state)
        else:
            connor.defend(terminator)
            result.append(new_state)

    return action, result

def expand(node, problem):
    successors = []
    action, result = successor_function(node.state)
    for x in range(len(action)):
        s = Node(None)
        s.parent = node
        s.action = action[x]
        s.state = result[x]
        s.path_cost = node.path_cost + 1
        s.depth = node.depth + 1
        successors.append(s)
        node.children.append(s)
    #for x in range(len(successors)):
    #    print('Successor: ' + str(successors[x].action))
    print(node.children)
    return successors

def solution(node):
    action_sequence = []
    current_node = node
    while current_node.parent != None:
        action_sequence.append(current_node.action)
        current_node = current_node.parent
    return action_sequence

def bfs(problem, fringe):
    initial_node = Node(problem)
    fringe.insert(initial_node)

    solution_found = False
    while solution_found == False:
        if fringe.head == None:
            return None
        node = fringe.pop()

        print('Connor: ' + str(node.state.connor.hp))
        print('Arnold: ' + str(node.state.terminator.hp))
        print('Arnold Defense: ' + str(node.state.terminator.defense))
        print('Depth: ' + str(node.depth))
        print('Path Cost: ' + str(node.path_cost))
        print('Action: ' + str(node.action))
        print('...')
        #input()

        if goal_test(node.state) == True:
            return solution(node)
        else:
            if node.state.connor.death == False:
                fringe.insert_all(expand(node, problem))

def ids(problem, fringe, next_gen, depth):
    initial_node = Node(problem)
    fringe.insert(initial_node)

    solution_found = False
    while solution_found == False:
        if fringe.head == None:
            return None
        node = fringe.get_last()


        if node.depth < depth:
            if len(node.children) > 0:
                for child in node.children:
                    if child not in fringe.ranged_list():
                        node = fringe.pop_last()
                        print(node)
                        if goal_test(node.state) == True:
                            return solution(node)
            elif len(fringe.queue) <= 0:
                depth += depth
                if len(next_gen) > 0:
                    for x in range(len(next_gen)):
                        fringe.insert(next_gen.pop())
            else:
                fringe.insert_all(expand(node, problem))
        elif node.depth == depth:
            node = fringe.pop_last()
            next_gen.insert(node)
            if goal_test(node.state) == True:
                return solution(node)

        print('Connor: ' + str(node.state.connor.hp))
        print('Arnold: ' + str(node.state.terminator.hp))
        print('Arnold Defense: ' + str(node.state.terminator.defense))
        print('Depth: ' + str(node.depth))
        print('Path Cost: ' + str(node.path_cost))
        print('Action: ' + str(node.action))
        print('...')
        input()


def tree_search(problem, fringe, initial=False):
    if initial == True:
        initial_node = Node(problem)
        fringe.insert(initial_node)

    if fringe.head == None:
        return None
    node = fringe.pop()

    if goal_test(node.state) == True:
        return solution(node)
    else:
        if node.state.connor.death == False:
            fringe.insert_all(expand(node, problem))
