import matplotlib.pyplot as plt


def plot_image(image, filtered_image):
    filtered_image, cmap = filtered_image

    fig, axes = plt.subplots(1, 2, figsize=(100, 80))
    original, new_image = axes.ravel()

    # Setting up original image
    original.imshow(image)
    original.axis('off')
    original.set_title("Original")

    # Setting up filtered image
    new_image.imshow(filtered_image,cmap=cmap)
    new_image.axis('off')
    new_image.set_title("Filtered Image")

    plt.show()




