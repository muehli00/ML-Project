# In this exercise, we will load and standardize (zero mean, unit variance) each image by the
# global mean and standard deviation of each color channel.


import os
import glob
from PIL import Image
import numpy as np
import hashlib
import shutil



class ImageStandardizer():
    def __init__(self, input_dir: str):
        # The init method gets all .jpg files from the input_dir

        self.input_dir = os.path.abspath(input_dir)
        paths = sorted(glob.glob(os.path.join(self.input_dir, "**"), recursive=True))
        self.files = [x for x in paths if x.endswith('.jpg')]
        self.mean = None
        self.std = None

        if not self.files:
            raise ValueError

    def analyze_images(self):
        for file in self.files:
            try:
                image_ = Image.open(file)
                arr = np.array(image_)
                self.std = (arr.std(axis=(0, 1)))
                self.mean = (arr.mean(axis=(0, 1)))
                print(self.mean)
            except OSError:
                print(f'Image {self.files}')



    def get_standardized_images(self):
        pass









if __name__ == "__main__":
    ImageStandardizer = ImageStandardizer(input_dir='unittest\\unittest_input_1')
    ImageStandardizer.analyze_images()

    for path in ImageStandardizer.files:
        if path.endswith('.jpg'):#
            print(path)
    # print(ImageStandardizer.image_files)
