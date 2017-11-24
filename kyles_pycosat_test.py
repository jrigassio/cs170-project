import pycosat
cnf = [[1, -5, 4], [-1, 5, 3, 4]]
print(pycosat.solve(cnf))
