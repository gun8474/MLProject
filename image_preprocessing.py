import os
import face_recognition
from PIL import Image
from os import listdir
from pathlib import Path

import cv2
import numpy as np

def createFoledr(dir):
    try:
        if not os.path.exists(dir):
            os.makedirs(dir)
    except OSError:
        print('Error: Creating directory. ' + dir)

def find_face(save_dir, name, image_fname, image_path):
    image = face_recognition.load_image_file(image_path)

    face_locations = face_recognition.face_locations(image)

    for face_location in face_locations:
        top, right, bottom, left = face_location

        face_image = image[top:bottom, left:right]
        pil_image = Image.fromarray(face_image)

        # pil_image.show(
        createFoledr(save_dir + name)
        pil_image.save(save_dir + name + '/' + image_fname, "JPEG")

if __name__ == "__main__":
    total_image_path = []
    image_dir = Path('C:/Users/USER/prlab/AtoZ/MLProject1/image')
    people_list = os.listdir(image_dir)
    save_dir = 'C:/Users/USER/prlab/AtoZ/MLProject1/face_image/'

    for people_list in people_list:
        image_list = os.listdir(os.path.join(image_dir, people_list))
        for image in image_list:
            image_path = os.path.join(image_dir, people_list, image)
            name = image_path.split('\\')[-2]
            image_fname = image_path.split('\\')[-1]

            find_face(save_dir, name, image_fname, image_path)




