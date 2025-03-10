import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QGraphicsView
from PyQt5.QtCore import Qt
from view import PacmanParams, PacmanScene
from controller import PacmanController

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mini-Pacman")
        
        # Create central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QHBoxLayout(central_widget)
        
        # Create controller
        self.controller = PacmanController()
        
        # Create and setup parameters widget
        self.params = PacmanParams()
        self.params.start_button.clicked.connect(self.start_game)
        self.params.stop_button.clicked.connect(self.stop_game)
        layout.addWidget(self.params)
        
        # Create and setup game scene and view
        self.scene = PacmanScene()
        self.view = QGraphicsView(self.scene)
        self.view.setFixedSize(520, 520)
        layout.addWidget(self.view)
        
        # Connect controller's refresh_views to scene's refresh
        self.controller.refresh_views = lambda: self.scene.refresh(self.controller)
        
    def start_game(self):
        width = self.params.grid_width.value()
        height = self.params.grid_height.value()
        nb_ghosts = self.params.ghosts_number.value()
        self.controller.start(width, height, nb_ghosts)
        self.scene.refresh(self.controller)
        
    def stop_game(self):
        self.controller.stop()
        
    def move_pacman(self, x, y):
        self.controller.move_pacman(x, y)
        
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_P:
            self.controller.process_keypress('P')

if __name__ == '__main__':
    try:
        app = QApplication(sys.argv)
        window = MainWindow()
        window.show()
        sys.exit(app.exec_())
    except Exception as e:
        print(f"Error starting game: {e}", file=sys.stderr)
        sys.exit(1)
