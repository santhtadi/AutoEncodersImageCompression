import cv2
import os
from tqdm import tqdm

images = os.listdir("./raw_data")


# create gray 28x28 images
def create_gray_28x28():
    for img in tqdm(images):
        inp = cv2.imread("./raw_data/" + img, 0)
        inp_resized = cv2.resize(inp, (28, 28))
        cv2.imwrite("./resized_28x28_gray/" + img, inp_resized)


# create color 28x28 images
# create color 9x28x28 splits
# create gray 128x128
def create_no_resize_gray():
    for img in tqdm(images[0:42000]):
        inp = cv2.imread("./raw_data/" + img, 0)
        cv2.imwrite("./gray_128x128/" + img, inp)


if __name__ == "__main__":
    # create_gray_28x28()
    create_no_resize_gray()
