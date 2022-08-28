class DimensionError(Exception):
    def __init__(self, message, shape):
        self.message = message
        self.shape = shape
        
        super().__init__(self.message)
        
    def __str__(self):
        return f'Not able to {self.message} with dimensions {self.shape}'

class LocationError(Exception):
    def __init__(self, message, location, *args):
        self.message = message
        self.location = location
        self.dimensions = args

        super().__init__(self.message)

    def __str__(self):
        return f'Cannot {self.message} with location {self.location} within dimensions {[i for i in self.dimensions]}'