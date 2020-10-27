import matplotlib.pyplot as plt
from matplotlib import image as Image
import cv2
import numpy as np
from pathlib import Path
import os
from typing import List, Union

def plot_images(images, cols=3, cell_size=5):
    N = len(images)
    assert(N > 0)
    rows = int(np.ceil(1.0 * N / cols))    
    fig = plt.figure(figsize=(cell_size*cols, cell_size*rows))
    for i in range(1, cols*rows + 1):
        idx = i - 1
        image = images[idx]
        title = str(idx)
        if type(image) == str or type(image) == type(Path()):
            image = str(image)
            assert(os.path.exists(image))
            title = title + ": " + image
            image = Image.imread(image)
        ax = fig.add_subplot(rows, cols, i)
        ax.set_title(title)
        plt.imshow(image)
    plt.show()
