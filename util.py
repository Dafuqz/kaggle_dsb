# !/usr/local/bin/python
import glob
from PIL import Image

def padimg(arr, max_h=2048, max_w=2048):
    print('call to',self)
def preprocess():
    #if img avg colour not approx grayscale
    #invert
    #add rotation / noise / contrast
    print('call to',self)
def next_miniBatch():
    print('call to',self)
def next_set(height,width):
    print('call to',self)
def get_label():
    print('call to',self)
def get_img():
    print('call to',self)
def crawl_path(path):
    db = []
    for __file in glob.iglob(path + '/*/*/*.*'):
        im = Image.open(__file)
        print([__file,im.size[0],im.size[1]])
        db.append([__file,im.size[0],im.size[1]])
    return db
