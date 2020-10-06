import os
from tqdm import tqdm
import shutil
for path, subdirs, files in tqdm(os.walk("./ffhq-dataset/dataset/thumbnails128x128")):
    for name in files:
        shutil.copy("/".join(os.path.join(path, name).split("\\")), os.path.join("./raw_data", name))
