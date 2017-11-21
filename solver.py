import argparse
import random
"""
======================================================================
  Complete the following function.
======================================================================
"""

def solve(num_wizards, num_constraints, wizards, constraints):
    """
    Write your algorithm here.
    Input:
        num_wizards: Number of wizards
        num_constraints: Number of constraints
        wizards: An array of wizard names, in no particular order
        constraints: A 2D-array of constraints,
                     where constraints[0] may take the form ['A', 'B', 'C']i

    Output:
        An array of wizard names in the ordering your algorithm returns
    """

    """
    ordering: a mapping from character names to indices, wizards is the inverse mapping
    """
    random.shuffle(wizards)
    ordering = dict(zip(wizards, range(len(wizards))))
    i = 0
    best_score = 0
    constraints = sorted(constraints, key = lambda x: abs(ordering[x[0]]-ordering[x[1]]))
    for constraint in constraints:
        if ordering[constraint[2]] > min(ordering[constraint[0]], ordering[constraint[1]]) and ordering[constraint[2]] < max(ordering[constraint[1]], ordering[constraint[0]]):
            best_score += 1
    threshold = 0.9
    while True:
        done = True
        #random.shuffle(constraints)
        if i % 20 == 0:
            print("on attempt ", i, " num not satisified: ", best_score, " threshold: ", threshold)
            print(wizards)
            threshold = threshold * 0.999
        if i % 15000 == 0:
            threshold = 0.9
        i += 1
        #looping over all constraints
        for constraint in constraints:
            if ordering[constraint[2]] > min(ordering[constraint[0]], ordering[constraint[1]]) and ordering[constraint[2]] < max(ordering[constraint[1]], ordering[constraint[0]]):
                #all places we ccould possibly swap our item
                choice_range = list(range(min(ordering[constraint[0]], ordering[constraint[1]])+1)) + list(
                    range(max(ordering[constraint[0]], ordering[constraint[1]]), len(wizards)))

                choice, ct = choice_range[0], 100000
                #considering all places we can swap the third element to
                for elem in choice_range:
                    new_ct = 0

                    #swapping
                    tmp = ordering[constraint[2]]
                    wizards[tmp], wizards[elem] = wizards[elem], wizards[tmp]
                    ordering[wizards[tmp]], ordering[wizards[elem]] = tmp, elem

                    for constraint in constraints:
                        if ordering[constraint[2]] > min(ordering[constraint[0]], ordering[constraint[1]]) and ordering[constraint[2]] < max(ordering[constraint[1]], ordering[constraint[0]]):
                            new_ct += 1

                    #swapping back
                    tmp = ordering[constraint[2]]
                    wizards[tmp], wizards[elem] = wizards[elem], wizards[tmp]
                    ordering[wizards[tmp]], ordering[wizards[elem]] = tmp, elem

                    #update count
                    if new_ct <= ct:
                        choice, ct = elem, new_ct
                #update count if better
                coin = random.random()
                if coin < threshold:
                    choice = random.choice(range(len(wizards)))
                    tmp = ordering[constraint[2]]
                    wizards[tmp], wizards[choice] = wizards[choice], wizards[tmp]
                    ordering[wizards[tmp]], ordering[wizards[choice]] = tmp, choice
                elif ct <= best_score:
                    best_score = ct
                    tmp = ordering[constraint[2]]
                    wizards[tmp], wizards[choice] = wizards[choice], wizards[tmp]
                    ordering[wizards[tmp]], ordering[wizards[choice]] = tmp, choice
        if best_score == 0:
            break
#ordering for input 3 ['Adan', 'Tamara', 'Zoey', 'Caroline', 'Aubrey', 'Gregg', 'Brayan', 'Rylie', 'Emma', 'Angel', 'Logan', 'Debra', 'Amir', 'Prince', 'Marquis', 'Joselyn', 'Jonah', 'Kiera', 'Faith', 'Ron']

    return wizards


"""
======================================================================
   No need to change any code below this line
======================================================================
"""

def read_input(filename):
    with open(filename) as f:
        num_wizards = int(f.readline())
        num_constraints = int(f.readline())
        constraints = []
        wizards = set()
        for _ in range(num_constraints):
            c = f.readline().split()
            constraints.append(c)
            for w in c:
                wizards.add(w)

    wizards = list(wizards)
    return num_wizards, num_constraints, wizards, constraints

def write_output(filename, solution):
    with open(filename, "w") as f:
        for wizard in solution:
            f.write("{0} ".format(wizard))

if __name__=="__main__":
    parser = argparse.ArgumentParser(description = "Constraint Solver.")
    parser.add_argument("input_file", type=str, help = "___.in")
    parser.add_argument("output_file", type=str, help = "___.out")
    args = parser.parse_args()

    num_wizards, num_constraints, wizards, constraints = read_input(args.input_file)
    solution = solve(num_wizards, num_constraints, wizards, constraints)
    write_output(args.output_file, solution)
