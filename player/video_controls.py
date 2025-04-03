import cv2
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QFileDialog, QSlider
from PyQt5.QtCore import Qt

class VideoControls:
    def __init__(self, player):
        self.player = player

    def choose_video(self):
        self.player.filename, _ = QFileDialog.getOpenFileName(self.player, "Choose Video", "", "Video Files (*.mp4 *.avi *.mov)")
        if self.player.filename:
            self.player.cap = cv2.VideoCapture(self.player.filename)
            if not self.player.cap.isOpened():
                print("Unable to open video!")
                return
            self.player.frame_count = int(self.player.cap.get(cv2.CAP_PROP_FRAME_COUNT))
            self.player.frame_rate = int(self.player.cap.get(cv2.CAP_PROP_FPS))
            self.player.ui.slider.setMaximum(self.player.frame_count - 1)
            self.player.ui.slider.setValue(0)
            self.display_frame(0)

    def prev_frame(self):
        if self.player.cap:
            current_frame = self.player.ui.slider.value()
            if current_frame > 0:
                self.display_frame(current_frame - 1)

    def play_video(self):
        if self.player.cap:
            if not self.player.playing:
                self.player.ui.play_btn.setText("Pause")
                self.player.playing = True
                self.player.timer.start(int((1000 // self.player.frame_rate) / self.player.playback_speed))
            else:
                self.player.ui.play_btn.setText("Play")
                self.player.playing = False
                self.player.timer.stop()

    def next_frame(self):
        if self.player.cap:
            current_frame = self.player.ui.slider.value()
            if current_frame < self.player.frame_count - 1:
                self.display_frame(current_frame + 1)
            else:
                self.player.ui.play_btn.setText("Play")
                self.player.playing = False
                self.player.timer.stop()

    def display_frame(self, frame_number):
        self.player.cap.set(cv2.CAP_PROP_POS_FRAMES, frame_number)
        ret, frame = self.player.cap.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            height, width, channel = frame.shape
            qimg = QImage(frame.data, width, height, channel * width, QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(qimg)
            self.player.ui.video_display.setPixmap(pixmap)
            self.player.ui.slider.setValue(frame_number)
            self.player.ui.frame_label.setText(f"Frame: {frame_number}")

    def change_speed(self, value):
        self.player.playback_speed = value / 10.0
        self.player.ui.speed_label.setText(f"Speed: {self.player.playback_speed:.1f}x")
        if self.player.playing:
            self.player.timer.start(int((1000 // self.player.frame_rate) / self.player.playback_speed))
