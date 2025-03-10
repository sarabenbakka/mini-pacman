from PyQt5.QtWidgets import QWidget, QSpinBox, QPushButton, QFormLayout, QGraphicsScene, QGraphicsView
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QColor, QBrush, QPen

class PacmanParams(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_ui()
        
    def setup_ui(self):
        layout = QFormLayout()
        
        # Create spin boxes for grid dimensions and ghosts
        self.grid_width = QSpinBox()
        self.grid_width.setRange(10, 50)
        self.grid_width.setValue(20)
        
        self.grid_height = QSpinBox()
        self.grid_height.setRange(10, 50)
        self.grid_height.setValue(20)
        
        self.ghosts_number = QSpinBox()
        self.ghosts_number.setRange(1, 10)
        self.ghosts_number.setValue(3)
        
        # Create buttons
        self.start_button = QPushButton("START")
        self.stop_button = QPushButton("STOP")
        
        # Add widgets to layout
        layout.addRow("Grid Width", self.grid_width)
        layout.addRow("Grid Height", self.grid_height)
        layout.addRow("Ghosts Number", self.ghosts_number)
        layout.addRow(self.start_button)
        layout.addRow(self.stop_button)
        
        self.setLayout(layout)

class PacmanScene(QGraphicsScene):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setSceneRect(0, 0, 512, 512)
        self.cell_size = 25
        
    def refresh(self, controller):
        self.clear()
        
        # Draw game board background
        width = controller.width * self.cell_size
        height = controller.height * self.cell_size
        
        # Draw background and border
        self.addRect(0, 0, width, height, 
                    QPen(Qt.black), 
                    QBrush(Qt.lightGray))
        
        # Draw Pacman
        if controller.pacman:
            x = controller.pacman.x * self.cell_size
            y = controller.pacman.y * self.cell_size
            self.addEllipse(x, y, self.cell_size, self.cell_size,
                          QPen(Qt.black),
                          QBrush(Qt.yellow))
        
        # Draw ghosts
        for ghost in controller.ghosts:
            x = ghost.x * self.cell_size
            y = ghost.y * self.cell_size
            self.addEllipse(x, y, self.cell_size, self.cell_size,
                          QPen(Qt.black),
                          QBrush(Qt.red))
    
    def mousePressEvent(self, event):
        x = int(event.scenePos().x() / self.cell_size)
        y = int(event.scenePos().y() / self.cell_size)
        self.parent().move_pacman(x, y)
        
    def keyPressEvent(self, event):
        self.parent().keyPressEvent(event)
