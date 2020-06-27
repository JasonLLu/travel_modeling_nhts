import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cv2


# count digits
def digit_counts(list_, SAT = False):
    # output the number of items with 10 and 11 digits. 
    # give warning if the items have number of digits different from 10 and 11.
    d_10 = 0
    d_11 = 0

    if SAT:
        for idx in np.arange(len(list_)):
            if len(list_[idx]) == 17: # 10+3+4 because 3 represents "wms" and 4 represents ".jpg" ...
                d_10 += 1
            elif len(list_[idx]) == 18: # 11+3+4 because 3 represents "wms" and 4 represents ".jpg" ...
                d_11 += 1
        if d_10 + d_11 < len(list_):
            print("Warning: Total sum does not add up...")
    else:
        for idx in np.arange(len(list_)):
            if len(list_[idx]) == 10:
                d_10 += 1
            elif len(list_[idx]) == 11:
                d_11 += 1
        if d_10 + d_11 < len(list_):
            print("Warning: Total sum does not add up...")
            
    return d_10, d_11

# imshow
def imshow(image, *args, **kwargs):
    if len(image.shape) == 3:
      # Height, width, channels
      # Assume BGR, do a conversion since 
      image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    else:
      # Height, width - must be grayscale
      # convert to RGB, since matplotlib will plot in a weird colormap (instead of black = 0, white = 1)
      image = cv2.cvtColor(image, cv2.COLOR_GRAY2RGB)
    # Draw the image
    plt.imshow(image, *args, **kwargs)
    # We'll also disable drawing the axes and tick marks in the plot, since it's actually an image
    plt.axis('off')
    # Make sure it outputs
    plt.show()








