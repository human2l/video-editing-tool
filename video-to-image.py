import os
import cv2

# Define the input and output directories
input_dir = './input'
output_dir = './output'

# Find the video file in the input directory
video_path = None
for filename in os.listdir(input_dir):
    if filename.endswith('.mp4') or filename.endswith('.avi') or filename.endswith('.mkv'):
        video_path = os.path.join(input_dir, filename)
        break

# Check if a video file was found
if video_path is None:
    print('Error: No video file found in input directory')
    exit()

# Open the video file
cap = cv2.VideoCapture(video_path)

# Check if the video file was successfully opened
if not cap.isOpened():
    print('Error: Could not open video file')
    exit()

# Read and save each frame as an image
frame_count = 0
skips = 2
while True:
    # Read the next frame from the video
    ret, frame = cap.read()

    # Check if the end of the video has been reached
    if not ret:
        break

    # Save every third frame as an image
    if frame_count % skips == 0:
        frame_path = os.path.join(output_dir, 'frame_' + str(frame_count) + '.jpg')
        cv2.imwrite(frame_path, frame)

    # Increment the frame count
    frame_count += 1

# Release the video capture object and close all windows
cap.release()
cv2.destroyAllWindows()

# Print the number of frames extracted
print('Frames extracted:', frame_count // skips)
