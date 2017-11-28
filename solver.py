import argparse
import random
import pycosat
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

    wizard_list = list(wizards)
    wizard_pos = {}
    pos_wizard = {}
    cnf_array = []
    count = 1

    for i in range(num_wizards-1):
        for j in range(i+1, num_wizards):
            wizard_pos[(wizards[i], wizards[j])] = count
            wizard_pos[(wizards[j], wizards[i])] = -count
            pos_wizard[-count] = (wizards[j], wizards[i])
            pos_wizard[count] = (wizards[i], wizards[j])
            count += 1
    for i in range(num_wizards-2):
        for j in range(i+1, num_wizards-1):
            for k in range(j+1, num_wizards):
                    a = (wizard_list[i], wizard_list[j])
                    b = (wizard_list[j], wizard_list[k])
                    c = (wizard_list[k], wizard_list[i])
                    cnf_array.append([wizard_pos[a], wizard_pos[b], wizard_pos[c]])
                    d = (wizard_list[j], wizard_list[i])
                    e = (wizard_list[k], wizard_list[j])
                    f = (wizard_list[i], wizard_list[k])
                    cnf_array.append([wizard_pos[d], wizard_pos[e], wizard_pos[f]])
    for con in constraints:
        first_wiz =  con[0]
        second_wiz = con[1]
        third_wiz = con[2]
        x = (first_wiz, second_wiz)
        y = (second_wiz, third_wiz)
        z = (first_wiz, third_wiz)
        cnf_array.append([-wizard_pos[y], wizard_pos[z]])
        cnf_array.append([wizard_pos[y], -wizard_pos[z]])
    # print("wiz list:", wizard_list)
    satisfying_assignment = pycosat.solve(cnf_array)
    # print(satisfying_assignment)

    graph = {}
    for item in satisfying_assignment:
        # print("constraint:", pos_wizard[item])
        if pos_wizard[item][0] in graph:
            graph[pos_wizard[item][0]].append(pos_wizard[item][1])
        else:
            graph[pos_wizard[item][0]] = [pos_wizard[item][1]]
    for wizard in wizard_list:
        if wizard not in graph:
            graph[wizard] = []
    ordering, visited = [], set()
    stack = []
    # print(graph)

    visited, rec = set(), set()
    failed = False
    toppl = []

    def postorder_traversal(start):
        visited.add(start)
        rec.add(start)
        for neighbor in graph[start]:
            if neighbor in rec:
                failed = True
                return
            if neighbor not in visited:
                postorder_traversal(neighbor)
        toppl.append(start)
        rec.remove(start)

    for i in range(num_wizards):
        if not wizards[i] in visited:
            postorder_traversal(wizards[i])
    return toppl if not failed else []



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
