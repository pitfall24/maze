from exceptions import LocationError, PathError
from util import out_of_bounds

class Path:
    def __init__(self, shape, start):
        self.shape = shape
        self.path = Node(self.shape, start)

    def add_connections(self, connections):
        for i in connections:
            self.path.connect(i)

    def add_connection(self, connection):
        self.path.connect(connection)

class Node:
    def __init__(self, shape, location, connections=None):
        self.shape = shape
        self.location = self._locate(location)
        self.connections = self._connect(connections) if connections else []

    def connect(self, connection):
        if out_of_bounds(i, self.shape):
            raise LocationError('assign connection location', i, self.shape)
        else:
            self.connections.append(i)


    def _locate(self, location):
        if out_of_bounds(loc, self.shape):
            raise LocationError('assign node location', location, self.shape)
    
        return location

    def _connect(self, connections):
        if len(connections) >= 2 ** len(self.shape):
            raise PathError(f'Too many connections for {len(self.shape)} dimensional space')
        else:
            for i in connections:
                if out_of_bounds(i, self.shape):
                    raise LocationError('assign connection location', i, self.shape)

        return connections