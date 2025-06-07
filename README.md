# DataVision Player 🎥

**DataVision Player** is a user-friendly desktop application built with PyQt5 and OpenCV for seamless video playback and synchronized data visualization. Designed for researchers and analysts, it allows you to load a video and automatically link it with CSV data files from the same directory. For any selected video frame, the app extracts and visualizes relevant data from all CSVs, making it easy to analyze time-synced experimental or observational data.

With features like frame-by-frame navigation, adjustable playback speed, and interactive graph plotting, DataVision Player streamlines the process of exploring and presenting video-linked datasets.

## 🚀 Features  
✅ Load and play videos (MP4, AVI, MOV)  
✅ Frame-by-frame navigation (Previous, Next)  
✅ Adjustable playback speed (0.5x - 2.0x)  
✅ Data selection for visualization  

## 🔧 Technologies Used  
- **Python** (PyQt5, OpenCV)  
- **GUI**: PyQt5  
- **Video Processing**: OpenCV
- **Data Synchronization**: Pandas
- **Data visualization**: Matplotlib

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

## 🛠️ Build Instructions

Clone the repository:
git clone https://github.com/your-username/DataVision-Player.git
cd DataVision-Player

Install dependencies:
pip install -r requirements.txt

Build the application:
pyinstaller --name "DataVisionPlayer" --onefile --windowed main.py

Run the app:
After build completes, navigate to the dist/ folder and run:
./dist/DataVisionPlayer.exe

## 🛠️ Run the Application without Build
Go to dist/DataVisionPlayer.exe and double click on it