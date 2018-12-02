from environment import State
from utils import Node, Queue, bubble_sort

def goal_test(state):
    # Initiate the function to check death
    state.connor.check_dead()
    state.terminator.check_dead()

    # If Connor is alive but Terminator is not, return that there's a goal node
    if state.connor.death == False and state.terminator.death == True:
        return True

def successor_function(state):
    action = state.functions
    result = []

    # Simulate the actions, then return the state of the 2 actions
    for x in range(len(action)):
        # Create a new state with new values, very important so that the address in the RAM will be new
        new_state = State()
        new_state.connor.hp = state.connor.hp
        new_state.terminator.hp = state.terminator.hp
        new_state.terminator.defense = state.terminator.defense
        connor = new_state.connor
        terminator = new_state.terminator

        # Simulate the actions then append the result in new_state
        if action[x] == 'attack':
            connor.attack(terminator)
            result.append(new_state)
        else:
            connor.defend(terminator)
            result.append(new_state)

    return action, result

def expand(node):
    # Get the results of the successor functions first
    successors = []
    action, result = successor_function(node.state)

    # For every action done, create a new node from the existing node with different values based on [result]
    for x in range(len(action)):
        s = Node(None)
        s.parent = node
        s.action = action[x]
        s.state = result[x]
        s.path_cost = node.path_cost + 1
        s.depth = node.depth + 1
        successors.append(s)
        node.children.append(s)
    return successors

def best_fs_evaluator(node):
    cost = 0

    # Evaluate the cost based simply on HP, on if defense is False (meaning no progress is made) and the cost of death
    cost += node.state.terminator.hp
    if node.state.terminator.defense == False:
        cost += 1
    if node.state.connor.hp <= 0:
        cost += 3
    return cost

def a_star_evaluator(node):
    cost = 0
    # Criteria
    # 1 - Not too important, but affects path cost
    # 2 - Important, i.e. lower hp on h(n) etc.
    # 4 - Very critical factor, this node must not be taken
    # Why 4? It is to increase the cost of death, because if not then [death] functions will have an equal cost to winning functions
    # g(n), the cost to reach function based on current node
    if node.parent != None:
        if node.parent.state.terminator.defense == node.state.terminator.defense:
            cost += 1
        if node.parent.state.terminator.hp == node.state.terminator.hp:
            cost += 1
        if node.state.connor.hp <= 0:
            cost += 4

    # h(n)
    for x in range(node.state.terminator.hp):
        if node.state.terminator.defense == False:
            cost += 1
        cost += 2

    return cost

def solution(node):
    action_sequence = []
    current_node = node

    # Search bottom-up from the goal node to the originating node
    while current_node.parent != None:
        # Append the action of current_node at the start of the sequence
        action_sequence = [current_node.action] + action_sequence

        # Turn current_node into the parent of the current current_node
        current_node = current_node.parent
    return action_sequence

def bfs(problem, fringe):
    # If there is no node on fringe, make one
    if len(fringe.queue) <= 0:
        initial_node = Node(problem)
        fringe.insert(initial_node)

    # Pop the first node on the fringe
    node = fringe.pop()

    # Test if node is goal node, otherwise expand it and return the fringe for use
    # Return node to display progress
    if goal_test(node.state) == True:
        return True, solution(node), node
    else:
        if node.state.connor.death == False:
            fringe.insert_all(expand(node))
        return False, fringe, node

def ids(problem, fringe, next_gen, depth):
    # If there is no node on fringe, make one
    if len(fringe.queue) <= 0:
        initial_node = Node(problem)
        fringe.insert(initial_node)

    # Get the last
    node = fringe.get_last()

    # If node is not equal to the depth, do things; otherwise:
    if node.depth < depth:
        if len(node.children) > 0:
            # If node has children and they're not in the fringe, pop the node
            # It means if the child has been scanned/popped
            # A child can still exist even if it's not in the fringe, which is why it checks if the child is in the fringe
            # If it's not in the fringe, that means it's already been popped and thus, the parent shall be popped
            # Why? Because IDS is LIFO, and children are last in, thus they are first popped
            for child in node.children:
                if child not in fringe.ranged_list():
                    node = fringe.pop_last()

                    if goal_test(node.state) == True:
                        return True, solution(node), node, depth, next_gen

                    return False, fringe, node, depth, next_gen
        elif len(fringe.queue) <= 1 and len(next_gen.queue) > 0:
            # If the fringe has 1 or less nodes and next_gen has nodes
            # get to the next depth and start expanding the next_gen nodes
            depth += depth
            for x in range(len(next_gen.queue)):
                fringe.insert(next_gen.pop())
                return False, fringe, node, depth, next_gen
        else:
            # Else, expand it
            fringe.insert_all(expand(node))
            return False, fringe, node, depth, next_gen
    elif node.depth == depth:
        # Otherwise insert the node as the "next_gen" node
        # next_gen is the next generation of depth
        node = fringe.pop_last()
        next_gen.insert(node)
        if goal_test(node.state) == True:
            return True, solution(node), node, depth, next_gen
        return False, fringe, node, depth, next_gen

def best_fs(problem, fringe):
    # If there is no node on fringe, make one
    if len(fringe.queue) <= 0:
        initial_node = Node(problem)
        fringe.insert(initial_node)

    # If nodes don't have path cost for Greedy BFS, give them one
    for node in fringe.queue:
        if node.greed_cost == None:
            node.greed_cost = best_fs_evaluator(node)

    # Form a temporary priority queue
    best_fs_fringe = Queue()
    best_fs_fringe.insert_all(fringe.queue)

    # Sort them according to lowest path cost
    bubble_sort(best_fs_fringe)

    # Now do the good stuff
    # Get the first node in Greedy BFS fringe and then pop it on the main fringe
    greed_node = best_fs_fringe.pop()
    node = fringe.pop_specific(greed_node)

    # If the node is the goal, return it as goal; otherwise expand it
    if goal_test(node.state) == True:
        return True, solution(node), node
    else:
        if node.state.connor.death == False:
            fringe.insert_all(expand(node))
        return False, fringe, node

def a_star_search(problem, fringe):
    # If there is no node on fringe, make one
    if len(fringe.queue) <= 0:
        initial_node = Node(problem)
        fringe.insert(initial_node)

    # If nodes don't have path cost for A* Search, give them one
    for node in fringe.queue:
        if node.a_star_cost == None:
            node.a_star_cost = a_star_evaluator(node)

    # Form a temporary priority queue
    a_star_fringe = Queue()
    a_star_fringe.insert_all(fringe.queue)

    # Sort them according to lowest path cost
    bubble_sort(a_star_fringe, False)

    # Iterate over the sorted nodes, to check visually
    for nodes in a_star_fringe.queue:
        print('Node: ' + str(nodes.a_star_cost) + ' Depth: ' + str(nodes.depth) + ' Action: ' + str(nodes.action))

    # Now do the good stuff
    # Get the first node in A* fringe and then pop it on the main fringe
    greed_node = a_star_fringe.pop()
    node = fringe.pop_specific(greed_node)

    # If the node is the goal, return it as goal; otherwise expand it
    if goal_test(node.state) == True:
        return True, solution(node), node
    else:
        if node.state.connor.death == False:
            fringe.insert_all(expand(node))
        return False, fringe, node

def tree_search(problem, fringe, initial=False):
    # This function is a base function that will be kept here for the purposes of simply keeping it here because why not
    # a.k.a. backup plan just in case everything is ruined
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
            fringe.insert_all(expand(node))
