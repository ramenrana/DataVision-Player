from PyQt5.QtWidgets import QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QListWidget, QWidget, QSlider
from PyQt5.QtCore import Qt, QTimer

class UIComponents:
    def __init__(self, player):
        self.player = player
        central_widget = QWidget(player)
        player.setCentralWidget(central_widget)

        #print("Checking if player has controller:", hasattr(player, "controller"))
        #print("Checking if controller has choose_video:", hasattr(player.controller, "choose_video"))

        # Video display
        self.video_display = QLabel("Video Display")
        self.video_display.setMinimumSize(800, 500)
        self.video_display.setStyleSheet("background-color: white; border: 1px solid black;")
        self.video_display.setAlignment(Qt.AlignCenter)
        self.video_display.setScaledContents(True)

        # Video control buttons
        self.choose_video_btn = QPushButton("Choose Video", player)
        self.prev_btn = QPushButton("<<", player)
        self.play_btn = QPushButton("Play", player)
        self.next_btn = QPushButton(">>", player)
        self.slider = QSlider(Qt.Horizontal, player)
        self.frame_label = QLabel("Frame: 0", player)
        self.frame_label.setFixedHeight(15)

        # Playback speed slider
        self.speed_slider = QSlider(Qt.Horizontal, player)
        self.speed_slider.setMinimum(5)  # 0.5x speed
        self.speed_slider.setMaximum(20)  # 2.0x speed
        self.speed_slider.setValue(10)  # Default 1.0x speed
        self.speed_slider.valueChanged.connect(player.controller.change_speed)
        self.speed_label = QLabel("Speed: 1.0x", player)
        self.speed_label.setFixedHeight(20)

        # Data selection
        self.right_label = QListWidget()
        self.right_label.setSelectionMode(QListWidget.MultiSelection)
        self.right_label.setFixedWidth(300)  # Fixed initial width
        options = ['E2E_SeqCounter_OBJ', 'uiMsgCounter_OBJ', 'uiID_OBJ', 'uiMergeID_OBJ', 'eMaintenanceState_OBJ', 'fArelYStd_OBJ', 'fArelY_OBJ']
        self.right_label.addItems(options)
        self.plot_btn = QPushButton("Plot", player)

        # Layout setup
        video_layout = QVBoxLayout()
        video_layout.addWidget(self.video_display)

        control_layout = QHBoxLayout()
        control_layout.addWidget(self.choose_video_btn)
        control_layout.addWidget(self.prev_btn)
        control_layout.addWidget(self.play_btn)
        control_layout.addWidget(self.next_btn)

        speed_layout = QHBoxLayout()
        speed_layout.addWidget(QLabel("Speed:"))
        speed_layout.addWidget(self.speed_slider)
        speed_layout.addWidget(self.speed_label)

        data_layout = QVBoxLayout()
        data_layout.addWidget(self.right_label)
        data_layout.addWidget(self.plot_btn)
        
        main_layout = QVBoxLayout()
        main_layout.addLayout(video_layout)
        main_layout.addWidget(self.frame_label)
        main_layout.addLayout(control_layout)
        main_layout.addWidget(self.slider)
        main_layout.addLayout(speed_layout)

        overall_layout = QHBoxLayout()
        overall_layout.addLayout(main_layout)
        overall_layout.addLayout(data_layout)
        
        central_widget.setLayout(overall_layout)

        # Button connections
        self.choose_video_btn.clicked.connect(player.controller.choose_video)
        self.prev_btn.clicked.connect(player.controller.prev_frame)
        self.play_btn.clicked.connect(player.controller.play_video)
        self.next_btn.clicked.connect(player.controller.next_frame)