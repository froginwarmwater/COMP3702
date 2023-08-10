import sys
import copy
import time


LEFT = 0
RIGHT = 1
UP = 2
DOWN = 3


class EightPuzzle:

    def __init__(self, squares):
        self.squares = tuple(squares)

        idx = -1
        for i in range(len(self.squares)):
            if self.squares[i] == '_':
                idx = i
        self.idx = idx

    def __eq__(self, obj):
        if obj is None:
            return False
        return self.squares == obj.squares

    def __hash__(self):
        return hash(self.squares)

    def move_left(self):
        # implement left
        return None

    def move_right(self):
        # implement right
        return None

    def move_up(self):
        # implement up
        return None

    def move_down(self):
        # implement down
        return None

    def get_successors(self):
        successors = []

        if self.idx % 3 > 0:
            successors.append(self.move_left())
        else:
            successors.append(None)

        if self.idx % 3 < 2:
            successors.append(self.move_right())
        else:
            successors.append(None)

        if self.idx // 3 > 0:
            successors.append(self.move_up())
        else:
            successors.append(None)

        if self.idx // 3 < 2:
            successors.append(self.move_down())
        else:
            successors.append(None)

        return successors

    def num_inversions(self):
        # implement parity helper function
        return None

    def get_parity(self):
        # implement parity check
        return None

    def __str__(self):
        s = ""
        for c in self.squares:
            s += c
        return s


class ContainerEntry:
    def __init__(self, puzzle, parent, action_from_parent):
        self.puzzle = puzzle
        self.parent = parent
        self.action_from_parent = action_from_parent

    def get_successors(self):
        s = []
        suc = self.puzzle.get_successors()

        if suc[0] is not None:
            s.append(ContainerEntry(suc[0], self, LEFT))
        if suc[1] is not None:
            s.append(ContainerEntry(suc[1], self, RIGHT))
        if suc[2] is not None:
            s.append(ContainerEntry(suc[2], self, UP))
        if suc[3] is not None:
            s.append(ContainerEntry(suc[3], self, DOWN))

        return s

    def __eq__(self, obj):
        return self.puzzle == obj.puzzle


def bfs(initial, goal):
    # implement bfs
    return None


def dfs(initial, goal):
    # implement dfs
    return None


def main(arglist):
    # p1 = EightPuzzle("1348627_5")
    # p1 = EightPuzzle("281_43765")
    p1 = EightPuzzle("281463_75")
    p2 = EightPuzzle("1238_4765")
    
    # run bfs solution
    # run dfs solution
    

if __name__ == '__main__':
    main(sys.argv[1:])