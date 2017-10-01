from os import listdir
from os.path import isfile, join
from keras.preprocessing.image import ImageDataGenerator
from skimage.io import imread_collection


def profile_images(dir_path):
    """
    Calculates the profiles of images in a directory
    :param dir_path: The directory path of the images
    :return: ImageProdile containing max_dimensions, min_dimension, avg_dimension
    """
    # onlyfiles = [f for f in listdir(dir_path) if isfile(join(dir_path, f))]
    col = imread_collection(dir_path)
    print(col)
    return col


class ImageProfile:
    def __init__(self, max_dimension, min_dimension, avg_dimension):
        self.avg_dimension = avg_dimension
        self.min_dimension = min_dimension
        self.max_dimension = max_dimension
