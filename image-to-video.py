import os
import cv2

# Define the input and output directories
input_dir = './AI-output'
output_dir = './output-video'

# Find the frames in the input directory
frames = []
for filename in os.listdir(input_dir):
    if filename.endswith('.jpg'):
        frames.append(os.path.join(input_dir, filename))

# Sort the frames by their index in the file name
frames.sort(key=lambda x: int(x.split('_')[-1].split('.')[0]))

# Read the first frame to get the image dimensions
frame = cv2.imread(frames[0])
height, width, channels = frame.shape

# Define the output video path and properties
video_path = os.path.join(output_dir, 'output_video.mp4')
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
fps = 30.0
video_writer = cv2.VideoWriter(video_path, fourcc, fps, (width, height))

# Write each frame to the output video
for frame_path in frames:
    frame = cv2.imread(frame_path)
    for i in range(3):
        video_writer.write(frame)

# Release the video writer object and close all windows
video_writer.release()
cv2.destroyAllWindows()

# Print a message indicating the output video path
print('Output video saved to:', video_path)
