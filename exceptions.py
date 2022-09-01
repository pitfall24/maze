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

class PathError(Exception):
    def __init__(self, message, *args, **kwargs):
        self.message = message
        self.args = args
        self.kwargs = kwargs

    def __str__(self):
        return f'{self.message}{"\n" if self.args else ""}{", ".join(self.args)}{"\n" if self.kwargs else ""}{", ".join(f"{key}: {value}" for key, value in self.kwargs.items())}'

class ScopeError(Exception):
    def __init__(self, message, nums, scope1, scope2=None):
        self.message = message
        self.nums = nums
        self.scope1 = scope1
        self.scope2 = scope2
    
    def __str__(self):
        return f'Cannot {self.message} {self.nums} within scope{"s" if scope2 else ""} {self.scope1} {"or " if self.scope2 else ""}{self.scope2 if self.scope2 else ""}'