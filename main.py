from test import Test

from solver import Solver

if __name__ == '__main__':
    solver = Solver()
    test = Test(solver.run)
    test.run()
