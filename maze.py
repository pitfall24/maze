from exceptions import DimensionError, LocationError
from util import out_of_bounds
import numpy as np

class Maze:
    def __init__(self, *args, start=None, end=None):
        if args:
            self.shape = tuple(args)
        else:
            raise DimensionError('create maze', None)
        
        # -1 = Immovable wall used as padding
        #  0 = Regular wall
        #  1 = Movable space
        self.maze = np.pad(np.zeros([i - 2 for i in self.shape]), 1, constant_values=-1)

        self._setstart(start)
        self._setend(end)

    def generate(self, difficulty, sparsity):
        self._generate_solution(difficulty)
        self._generate_random(sparsity)

    def _generate_solution(self, difficulty):
        pass

    def _generate_random(self, sparsity):
        pass

    def _setstart(self, start):
        if start:
            if type(start) == int:
                start = (start, )
            if out_of_bounds(start, self.shape):
                raise LocationError('create start location', start, self.shape)
            else:
                self.start = start
        else:
            self.start = ([1 for _ in self.shape])

    def _setend(self, end):
        if end:
            if type(end) == int:
                end = (end, )
            if out_of_bounds(end, self.shape):
                raise LocationError('create end location', end, self.shape)
            else:
                self.end = end
        else:
            self.end = ([i - 2 for i in self.shape])
    
    def __getitem__(self, key):
        return self.maze[key]

    def __setitem__(self, key, value):
        self.maze[key] = value
    
    def __len__(self):
        return self.shape
    
    def __str__(self):
        if len(self.shape) == 2:
            return '\n'.join(' '.join(str(j) for j in i) for i in self.maze)
        else:
            raise DimensionError('print maze', self.shape)