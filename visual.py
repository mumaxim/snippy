import matplotlib.pyplot as plt
from matplotlib import image as Image
import cv2
import numpy as np
from pathlib import Path
import sys
from typing import List, Union
import os
from tqdm import tqdm
from time import time

import pandas as pd
from IPython.display import display, HTML

from pprint import PrettyPrinter
pprint = PrettyPrinter().pprint

def plot_images(images, cols=3, cell_size=5, titles=[], save_path="", bgr2rgb=True):
    videos_exts = ["mp4", "avi", "3gp", "mov", "mpeg", "mkv", "webm"]
    N = len(images)
    assert(N > 0)
    rows = int(np.ceil(1.0 * N / cols))   
    if len(images) < cols: cols = len(images)
    ln_len = 18 * cell_size // cols  # For long paths
    fig = plt.figure(figsize=(cell_size*cols, cell_size*rows))
    for i in range(1, cols*rows + 1):
        idx = i - 1
        if idx >= len(images): break
        image = images[idx]
        title = str(idx)
        if idx < len(titles): 
            if len(titles[idx]) > ln_len:
                title = title + ": " + titles[idx][:ln_len] + "\n" + titles[idx][ln_len:]
            else:
                title = title + ": " + titles[idx]  
        elif type(image) == str or type(image) == type(Path()):
            image = str(image)
            assert(os.path.exists(image))  
            if len(image) > ln_len:
                title = title + ": " + image[:ln_len] + "\n" + image[ln_len:]
            else:
                title = title + ": " + image
        if type(image) == str or type(image) == type(Path()):
            path = str(image)
            ext = path.split(".")[-1].lower()
            if not ext in videos_exts:
                image = cv2.imread(path)
            else:
                cap = cv2.VideoCapture(path)
                ret, image = cap.read()
                cap.release()
        ax = fig.add_subplot(rows, cols, i)
        ax.set_title(title)
        if bgr2rgb: image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        plt.imshow(image)
    plt.show()
    save_path = str(save_path)
    if len(save_path) > 0 and ".png" in save_path:
        Path(save_path).parent.mkdir(exist_ok=True, parents=True)
        fig.savefig(save_path)
