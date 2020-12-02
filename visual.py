import matplotlib.pyplot as plt
from matplotlib import image as Image
import cv2
import numpy as np
from pathlib import Path
import os
from typing import List, Union

from pprint import PrettyPrinter
pprint = PrettyPrinter().pprint

def plot_images(images, cols=3, cell_size=5):
    N = len(images)
    assert(N > 0)
    rows = int(np.ceil(1.0 * N / cols))   
    if len(images) < cols: cols = len(images)
    fig = plt.figure(figsize=(cell_size*cols, cell_size*rows))
    for i in range(1, cols*rows + 1):
        idx = i - 1
        image = images[idx]
        title = str(idx)
        if type(image) == str or type(image) == type(Path()):
            image = str(image)
            assert(os.path.exists(image))
            ln_len = 18 * cell_size // cols  # For long paths
            title = title + ": " + image[:ln_len] + "\n" + image[ln_len:]
            image = Image.imread(image)
        ax = fig.add_subplot(rows, cols, i)
        ax.set_title(title)
        plt.imshow(image)
    plt.show()
