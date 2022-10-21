def grayscale(image):
    r, g, b = image[:, :, 0], image[:, :, 1], image[:, :, 2]

    r_constant = 0.2126
    g_constant = 0.7152
    b_constant = 0.0722
    gamma = 1.04

    grayscale_image = (r_constant * r ** gamma) + (g_constant * g ** gamma) + (b_constant * b ** gamma)

    return grayscale_image, 'gray'


def sepia(image):
    r, g, b = image[:, :, 0], image[:, :, 1], image[:, :, 2]

    tr = (0.393 * r) + (0.769 * g) + (0.189 * b)
    tg = (0.349 * r) + (0.686 * g) + (0.168 * b)
    tb = (0.272 * r) + (0.534 * g) + (0.131 *b)

    sepia_image = tr + tg + tb

    return sepia_image, 'afmhot'

