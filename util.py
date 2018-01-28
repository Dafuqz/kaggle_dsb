# !/usr/local/bin/python
import glob
from PIL import Image

def padimg(arr, max_h=2048, max_w=2048):
    print('call to',self)
def preprocess(path):
    img = Image.open(path)
    img = img.convert('RGB')
    finalArr = []
    overall = 0
    w, h = img.size
    for i in range(0, w):
        finalArr.append([])
        for j in range(0, h):
            pixelr, pixelg, pixelb = img.getpixel((i, j))
            #print(pixelr, pixelg, pixelb)
            finalArr[i].append((pixelr + pixelg + pixelb) / 3)
            overall += (pixelr + pixelg + pixelb) / 3
    overall /= w * h
    if (overall > 25):
        for i in range(0, w):
            for j in range(0, h):
                finalArr[i][j] = 255 - finalArr[i][j]
    return finalArr
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

print(preprocess("00ae65c1c6631ae6f2be1a449902976e6eb8483bf6b0740d00530220832c6d3e.png"))
