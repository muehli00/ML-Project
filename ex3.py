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

        std = np.array([0, 0, 0], dtype=np.float32)
        mean = np.array([0, 0, 0], dtype=np.float32)
        for file in self.files:
            try:
                image_ = Image.open(file)
                arr = np.array(image_)
                std = std + (arr.std(axis=(0, 1)))
                mean = mean + (arr.mean(axis=(0, 1)))

            except OSError:
                print(f'Image {self.files} could not be opened')

        self.mean = mean/len(self.files)
        self.std = std/len(self.files)
        # print(self.std.dtype)

        return self.mean, self.std


    def get_standardized_images(self):
        if self.mean is None or self.std is None:
            raise ValueError

        for file in self.files:
            try:
                image_ = Image.open(file)
                standardized_data = np.array(((np.array(image_, dtype=np.float32) - self.mean)/self.std), dtype=np.float32)

                yield standardized_data



            except OSError:
                print(f'Image {self.files} could not be opened')











if __name__ == "__main__":
    # For testing...


    ImageStandardizer = ImageStandardizer(input_dir='unittest\\unittest_input_1')
    ImageStandardizer.analyze_images()
    gen = ImageStandardizer.get_standardized_images()
    for i, data in enumerate(gen):
        # print(data)
        if i > 2:
            break



    for path in ImageStandardizer.files:
        if path.endswith('.jpg'):#
            pass
            # print(path)
    # print(ImageStandardizer.image_files)

    imagedata = ImageStandardizer.get_standardized_images()
    print(type(imagedata))