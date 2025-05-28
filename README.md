# Pose Detection with Face Overlays

This Python application uses your webcam to detect your pose and adds fun overlays glasses  to your face in real-time.

## Requirements

- Python 3.7 or higher
- Webcam
- Required Python packages (listed in requirements.txt)

## Setup

1. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install the required packages:
```bash
pip install -r requirements.txt
```

## Usage

1. Make sure your webcam is connected and accessible
2. Run the application:
```bash
python app.py
```

3. Press 'q' to quit the application

## Features

- Real-time pose detection
- Face tracking
- Fun overlays (glasses and smoke)
- Mirror effect for natural interaction

## Note

Make sure the `images` folder contains the following files:
- spects.png (glasses overlay)
- cigar.png (smoke overlay)
- shahrukh.png (actor image) 