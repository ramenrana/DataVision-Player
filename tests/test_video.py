import unittest
from unittest.mock import MagicMock, patch
import sys
import os
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)


# Ensure the root project folder is in sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from player.video_controls import VideoControls


class MockSlider:
    def __init__(self):
        self.value_ = 0
        self.maximum = 100

    def setValue(self, val):
        self.value_ = val

    def value(self):
        return self.value_

    def setMaximum(self, max_val):
        self.maximum = max_val


class MockUI:
    def __init__(self):
        self.slider = MockSlider()
        self.play_btn = MagicMock()
        self.speed_label = MagicMock()
        self.video_display = MagicMock()
        self.frame_label = MagicMock()
        self.right_label = MagicMock()
        self.right_label.selectedItems = MagicMock(return_value=[])


class MockPlayer:
    def __init__(self):
        self.ui = MockUI()
        self.playing = False
        self.playback_speed = 1.0
        self.frame_rate = 30
        self.frame_count = 100
        self.timer = MagicMock()
        self.cap = MagicMock()
        self.cap.isOpened.return_value = True
        self.cap.read.return_value = (True, MagicMock())


class TestVideoControls(unittest.TestCase):

    def setUp(self):
        self.player = MockPlayer()
        self.controls = VideoControls(self.player)

    def test_change_speed(self):
        self.controls.change_speed(15)
        self.assertEqual(self.player.playback_speed, 1.5)
        self.player.ui.speed_label.setText.assert_called_with("Speed: 1.5x")

    def test_play_video_start(self):
        self.controls.play_video()
        self.assertTrue(self.player.playing)
        self.player.ui.play_btn.setText.assert_called_with("Pause")
        self.player.timer.start.assert_called()

    def test_play_video_pause(self):
        self.player.playing = True
        self.controls.play_video()
        self.assertFalse(self.player.playing)
        self.player.ui.play_btn.setText.assert_called_with("Play")
        self.player.timer.stop.assert_called()

    def test_prev_frame_bounds(self):
        self.player.ui.slider.setValue(0)
        self.controls.prev_frame()
        # Should not go below 0
        self.assertEqual(self.player.ui.slider.value(), 0)

    def test_next_frame_increments(self):
        self.player.ui.slider.setValue(10)
        self.controls.display_frame = MagicMock()
        self.controls.next_frame()
        self.controls.display_frame.assert_called_with(11)

    def test_next_frame_end(self):
        self.player.ui.slider.setValue(self.player.frame_count - 1)
        self.player.playing = True
        self.controls.next_frame()
        self.assertFalse(self.player.playing)
        self.player.timer.stop.assert_called()
        self.player.ui.play_btn.setText.assert_called_with("Play")
    
    @patch('player.video_controls.extract_and_plot_data')
    def test_plot_graph(self, mock_plot):
        self.player.filename = "dummy.mp4"
        mock_item = MagicMock()
        mock_item.text.return_value = "column1"
        self.player.ui.right_label.selectedItems.return_value = [mock_item]
        self.controls.csv = {'dummy': []}
        self.player.ui.slider.setValue(5)
        self.controls.plot_graph()
        mock_plot.assert_called()

if __name__ == '__main__':
    unittest.main()
