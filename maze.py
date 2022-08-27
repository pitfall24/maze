class Maze:
    def __init__(self, height=24, width=24):
        self.height = height + 2
        self.width = width + 2
        
        # -1 = Starting value
        #  0 = Movable space
        #  1 = Regular wall
        #  2 = Padding which represents static wall
        self.maze = [[-1 if 0 < j < self.width - 1 and 0 < i < self.height - 1 else 2 for j in range(self.width)] for i in range(self.height)]
    
    def __getitem__(self, key):
        if type(key) == int:
            return self.maze[key]
        elif type(key) == tuple:
            if type(key[0]) == int:
                return self.maze[key[0]][key[1]]
            if type(key[0]) == slice:
                return [i[key[1]] for i in self.maze[key[0]]]
        else:
            raise TypeError(f"'{type(key).__name__}' indexing not supported")
        
    def __setitem__(self, key, value):
        if type(key) == tuple:
            if type(key[0]) == int:
                if type(key[1]) == int:
                    self.maze[key[0]][key[1]] = value
                if type(key[1]) == slice:
                    for i in range(self.width)[key[1]]:
                        self.maze[key[0]][i] = value
            if type(key[0]) == slice:
                if type(key[1]) == int:
                    for i in range(self.height)[key[0]]:
                        self.maze[i][key[1]] = value
                if type(key[1]) == slice:
                    for i in range(self.height)[key[0]]:
                        for j in range(self.width)[key[1]]:
                            self.maze[i][j] = value
        else:
            raise TypeError(f"{'singular ' if type(key) == int else ''}'{type(key).__name__}' indexing not supported")
    
    def __str__(self):
        return '\n'.join(' '.join(str(j) for j in i) for i in self.maze)
        
    def __len__(self):
        return len(self.maze[0]), len(self.maze)
