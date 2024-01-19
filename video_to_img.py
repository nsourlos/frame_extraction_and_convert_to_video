# Prompt: split video into frames, process them, and then recreate video

import cv2
import os

video_path = 'C:/Users/soyrl/Desktop/result_voice_2_output.mp4'
output_folder = 'C:/Users/soyrl/Desktop/frames_new_2_upscale/' 

# processed_folder = 'C:/Users/soyrl/Desktop/processed_frames/'
# output_video_path = 'C:/Users/soyrl/Desktop/output_video.mp4'

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# if not os.path.exists(processed_folder):
#     os.makedirs(processed_folder)

#Step 1 - Takes ~19h in i7-6820HQ 2.70GHz - Should be parallelized
cap = cv2.VideoCapture(video_path)
frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

for frame_number in range(frame_count):
    ret, frame = cap.read()
    if not ret:
        break
    frame_filename = f'{output_folder}frame_{frame_number:04d}.jpg'
    cv2.imwrite(frame_filename, frame)

cap.release()


# #Step 2 - Extract masks from frames - Not needed anymore
# frame_files = os.listdir(output_folder)

# for frame_filename in frame_files:
#     frame_path = os.path.join(output_folder, frame_filename)
#     frame = cv2.imread(frame_path)
    
#     # Apply your processing here
#     processed_frame = ...  # Your processing code

#     processed_frame_filename = os.path.join(processed_folder, frame_filename)
#     cv2.imwrite(processed_frame_filename, processed_frame)


# # Step 3 - Recreate video - Try to parallelize if it takes long
# processed_frame_files = os.listdir(processed_folder)

# frame = cv2.imread(os.path.join(processed_folder, processed_frame_files[-1]))
# height, width, layers = frame.shape

# fourcc = cv2.VideoWriter_fourcc(*'mp4v')
# out = cv2.VideoWriter(output_video_path, fourcc, 30, (width, height))

# for processed_frame_filename in processed_frame_files:
#     frame = cv2.imread(os.path.join(processed_folder, processed_frame_filename))
#     out.write(frame)

# out.release()

