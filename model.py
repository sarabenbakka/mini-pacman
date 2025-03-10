from PyQt5.QtCore import QObject

class Entity(QObject):
    def __init__(self, x=0, y=0):
        super().__init__()
        self.x = x
        self.y = y
        
    def move(self, dx, dy, width, height):
        new_x = max(0, min(width - 1, self.x + dx))
        new_y = max(0, min(height - 1, self.y + dy))
        self.x = new_x
        self.y = new_y

class Pacman(Entity):
    def __init__(self, x=0, y=0):
        super().__init__(x, y)
