import sys
import numpy as np
from PIL import Image

width = 64
height = width


def idx_to_rad(idx, period):
    """convert pixel index to radians

    idx: the x or y coordinate

    period: the width/location of 2*pi
    """
    perc = idx / period
    return float(((np.pi * 2) * perc) / 2)


def convert_val_range(old_val, old_min, old_max, new_min, new_max):
    return ((old_val - old_min) / (old_max - old_min)) * (new_max - new_min) \
        + new_min


def gen_row_cos(length):
    row = np.zeros(length, np.ubyte)
    for i in range(length):
        row[i] = convert_val_range(
            np.cos((idx_to_rad(i, length))*np.pi), -1, 1, 0, 255)
    return row


def gen_row_sin(length):
    row = np.zeros(length, np.ubyte)
    for i in range(length):
        row[i] = convert_val_range(
            np.sin((idx_to_rad(i, length))*np.pi), -1, 1, 0, 255)
    return row


if __name__ == "__main__":
    hozln = gen_row_cos(width)
    stacked = np.tile(hozln, (height, 1))
    imgdata = Image.fromarray(stacked)
    imgdata.save(sys.argv[1])
