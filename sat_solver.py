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
    # wizard_position = {}
    wizard_pos = {}
    pos_wizard = {}
    cnf_array = []
    # for i in range (0, len(wizard_list)):
    #     wizard_numbers[wizard_list[i]] = i + 1
    count = 1
    for con in constraints:
        first_wiz =  con[0]
        second_wiz = con[1]
        third_wiz = con[2]
        x = (first_wiz, second_wiz)
        y = (second_wiz, third_wiz)
        z = (first_wiz, third_wiz)
        for a in (x, y, z):
            if a in wizard_pos:
                pass
            elif (a[1], a[0]) in wizard_pos:
                wizard_pos[a] = - wizard_pos[(a[1], a[0])]
                pos_wizard[-wizard_pos[(a[1], a[0])]] = (a[1], a[0])
                # pos_wizard[]
            else:
                wizard_pos[a] = count
                pos_wizard[count] = a
                count += 1

        # x = 100 * first_num + second_num
        # y = 100 * second_num + third_num
        # z = 100 * first_num + third_num
        cnf_array.append([-wizard_pos[x], wizard_pos[y]])
        cnf_array.append([wizard_pos[x], wizard_pos[z]])
    print("wiz list:", wizard_list)
    # for item in cnf_array:
    #     print("number:", item[0], item[1], "variable: ", pos_wizard[item[0]],  pos_wizard[item[1]])
    # print(cnf_array)
    satisfying_assignment = pycosat.solve(cnf_array)
    # print(satisfying_assignment)
    for item in satisfying_assignment:
        if item in pos_wizard:
            print("constraint:", pos_wizard[item])
    #fuck yeah
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
