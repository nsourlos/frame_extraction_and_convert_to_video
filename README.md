# Video to Individual Frames, Mask Extraction and conversion to Video again

[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
[![forthebadge](https://forthebadge.com/images/badges/uses-badges.svg)](https://forthebadge.com)

[![Maintenance](https://img.shields.io/badge/Maintained%3F-no-red.svg)]( https://github.com/nsourlos/semi-automated_installation_exe_msi_files-Windows_10)

> This [script](./video_to_img.py) is used to convert a video into a sequence of images. It uses the OpenCV library to read the video and extract the frames.
Then, it extracts some masks on those frames, and converts those masks back to a video. 

### Importing Required Libraries
The script begins by importing the necessary libraries. The OpenCV library (`cv2`) is used for video processing.

### Video Processing
The script opens the video file using `cv2.VideoCapture(video_path)`. It then gets the total number of frames in the video using `cap.get(cv2.CAP_PROP_FRAME_COUNT)`.

### Frame Extraction
The script then enters a loop that runs for the total number of frames in the video. In each iteration, it reads the next frame using `cap.read()`. If the frame is read successfully, it is saved as a JPEG image in the specified output folder with a filename in the format `frame_{frame_number:04d}.jpg`.

### Releasing Video Capture
After all frames have been processed, the script releases the video capture using `cap.release()`.

### Frame Processing (Commented Out)
The script also contains commented-out code for processing each frame after it has been extracted. This code reads each frame image, applies some processing (not specified in the provided code), and saves the processed frame in a separate folder. This part of the script is not currently being used.


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
 
