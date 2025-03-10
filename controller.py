from PyQt5.QtCore import QTimer, QObject
from model import Entity, Pacman
import random

class PacmanController(QObject):
    def __init__(self):
        super().__init__()
        self.ghosts = []
        self.pacman = None
        self.timer = None
        self.width = 20
        self.height = 20
        self.is_paused = False
        
        # Create and setup timer
        self.timer = QTimer()
        self.timer.timeout.connect(self.next)
        
    def start(self, width, height, nb_ghosts):
        self.width = width
        self.height = height
        self.ghosts = []
        
        # Create ghosts with random positions
        for _ in range(nb_ghosts):
            ghost = Entity(
                random.randint(0, width-1),
                random.randint(0, height-1)
            )
            self.ghosts.append(ghost)
            
        # Create pacman with random position
        self.pacman = Pacman(
            random.randint(0, width-1),
            random.randint(0, height-1)
        )
        
        # Start the timer
        self.timer.start(200)  # Update every 200ms
        
    def stop(self):
        if self.timer:
            self.timer.stop()
            
    def next(self):
        if self.is_paused:
            return
            
        # Move ghosts randomly
        for ghost in self.ghosts:
            dx = random.choice([-1, 0, 1])
            dy = random.choice([-1, 0, 1])
            ghost.move(dx, dy, self.width, self.height)
            
        # Check for collisions
        self.check_collisions()
        
        # Notify views to refresh
        self.refresh_views()
        
    def check_collisions(self):
        self.ghosts = [ghost for ghost in self.ghosts 
                      if not (ghost.x == self.pacman.x and ghost.y == self.pacman.y)]
            
        if not self.ghosts:
            self.stop()
            
    def move_pacman(self, x, y):
        if not self.is_paused and 0 <= x < self.width and 0 <= y < self.height:
            self.pacman.x = x
            self.pacman.y = y
            self.check_collisions()
            self.refresh_views()
            
    def process_keypress(self, key):
        if key == 'P':
            self.is_paused = not self.is_paused
            if not self.is_paused:
                self.timer.start(200)
            else:
                self.timer.stop()
                
    def refresh_views(self):
        # This will be connected to view's refresh method
        pass
