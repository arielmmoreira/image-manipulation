from skimage.io import imread, imsave


def read_image(path):
    image = imread(path)
    return image


def save_image(image, path):
    imsave(path, image)
