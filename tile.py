from enum import Enum

class Dir(Enum):
    UP = 1
    RIGHT = 2
    DOWN = 3
    LEFT = 4

class Tile: 
    def __init__(self, id, cost):
        self.id = id
        self.cost = cost

    def __str__(self):
        return f"Tile(id={self.id}, cost={self.cost})"
    
    def __repr__(self):
        return f"Tile(id={self.id}, cost={self.cost})"
    
    def can_connect(self):
        if self.id == '3':
            return (Dir.LEFT, Dir.RIGHT)
        if self.id == '5':
            return (Dir.UP, Dir.LEFT)
        if self.id == '6':
            return (Dir.RIGHT, Dir.UP)
        if self.id == '7':
            return (Dir.LEFT, Dir.RIGHT, Dir.UP)
        if self.id == '9':
            return (Dir.LEFT, Dir.DOWN)
        if self.id == 'A':
            return (Dir.RIGHT, Dir.DOWN)
        if self.id == 'B':
            return (Dir.LEFT, Dir.RIGHT, Dir.DOWN)
        if self.id == 'C':
            return (Dir.UP, Dir.DOWN)
        if self.id == 'D':
            return (Dir.LEFT, Dir.UP, Dir.DOWN)      
        if self.id == 'E':
            return (Dir.RIGHT, Dir.UP, Dir.DOWN)      
        if self.id == 'F':
            return (Dir.RIGHT, Dir.LEFT, Dir.UP, Dir.DOWN)   
    
    def connect(dir):
        if dir == Dir.LEFT:
            return (-1, 0)
        if dir == Dir.RIGHT:
            return (1, 0)
        if dir == Dir.UP:
            return (0, -1)
        if dir == Dir.DOWN:
            return (0, 1)
        
    def connectable(self):
        if self.id == '3':
            return (Dir.LEFT, Dir.RIGHT)
        if self.id == '5':
            return (Dir.DOWN, Dir.RIGHT)
        if self.id == '6':
            return (Dir.LEFT, Dir.DOWN)
        if self.id == '7':
            return (Dir.LEFT, Dir.RIGHT, Dir.DOWN)
        if self.id == '9':
            return (Dir.RIGHT, Dir.UP)
        if self.id == 'A':
            return (Dir.LEFT, Dir.UP)
        if self.id == 'B':
            return (Dir.LEFT, Dir.RIGHT, Dir.UP)
        if self.id == 'C':
            return (Dir.UP, Dir.DOWN)
        if self.id == 'D':
            return (Dir.RIGHT, Dir.UP, Dir.DOWN)      
        if self.id == 'E':
            return (Dir.LEFT, Dir.UP, Dir.DOWN)      
        if self.id == 'F':
            return (Dir.RIGHT, Dir.LEFT, Dir.UP, Dir.DOWN)   