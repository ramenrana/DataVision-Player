import unittest
from player.video_controls import VideoControls

class MockVideoPlayer:
    def __init__(self):
        self.playing = False  # Simulating VideoPlayer's playing attribute

class TestVideoControls(unittest.TestCase):
    def test_initial_state(self):
        player = MockVideoPlayer()  # Create a mock VideoPlayer
        controls = VideoControls(player)  # Pass mock player to VideoControls
        self.assertFalse(controls.player.playing)  # Check if playing is False

if __name__ == "__main__":
    unittest.main()
