# DataVision Player 🎥  
A feature-rich **PyQt-based video player** using **OpenCV** for smooth video playback, frame navigation, and speed control.  

## 🚀 Features  
✅ Load and play videos (MP4, AVI, MOV)  
✅ Frame-by-frame navigation (Previous, Next)  
✅ Adjustable playback speed (0.5x - 2.0x)  
✅ Data selection for visualization  

## 🔧 Technologies Used  
- **Python** (PyQt5, OpenCV)  
- **GUI**: PyQt5  
- **Video Processing**: OpenCV

## Folder Structure

DataVision Player/
│── main.py                 # Entry point of the application
│── player/
│   │── __init__.py         # Makes 'player' a package
│   │── video_player.py     # Contains Video Player class
│   │── video_controls.py
│── UI/
│   │── __init__.py         # Video control logic (play, pause, etc.)
│   │── ui_components.py    # UI layout components
│── tests/
│   │── test_video_player.py # Unit tests for Video Player
│── README.md               # Project documentation

