import colorsys
from random import shuffle


def make_bgr_colors(N, bright=True, randomize=False):
    """
    Generate random colors.
    To get visually distinct colors, generate them in HSV space then
    convert to RGB.
    """
    brightness = 1.0 if bright else 0.7
    hsv = [(i / N, 1, brightness) for i in range(N)]
    colors = list(map(__colorsysHsv2bgr, hsv))
    if randomize:
        shuffle(colors)
    return colors


def __colorsysHsv2bgr(hsv):
    r, g, b = colorsys.hsv_to_rgb(*hsv)
    return int(b * 255), int(g * 255), int(r * 255)
