from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import QTimer
from player.video_controls import VideoControls
from UI.ui_components import UIComponents

# class VideoPlayer is inherited from class QMainWindow
class VideoPlayer(QMainWindow):
    # Constructor(self represent instance of the class)
    def __init__(self):
        super().__init__()
        # Setting window title, possition and minimum size
        self.setWindowTitle("DataVision Player")
        self.setGeometry(350, 200, 1300, 700)
        self.setMinimumSize(1300, 700)

        # Initialize UI and Controls
        self.controller = VideoControls(self)
        self.ui = UIComponents(self)

        # setting up the user interface (UI), such as buttons, labels, and layouts.
        self.cap = None
        # QTimer is used to trigger functions at specified time intervals.
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.controller.next_frame)
        self.playing = False
        self.playback_speed = 1.0
