import cv2
import os

image_folder = 'ims/'
video_name = 'out.avi'

images = [img for img in os.listdir(image_folder) if img.endswith(".png")]
frame = cv2.imread(os.path.join(image_folder, images[0]))
height, width, layers = frame.shape

video = cv2.VideoWriter(video_name, 0, 30, (width,height))

for i, image in enumerate(images):
    video.write(cv2.imread(os.path.join(image_folder, image)))
    if i % 100 == 0:
        print(i)

cv2.destroyAllWindows()
video.release()