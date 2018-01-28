import csv
import math

def convertTo2D(h, w, array):
    toR = [ [0]*w for _ in range(h) ]
    for i in range(0, len(array), 2):
        for j in range(int(array[i]), int(array[i]) + int(array[i+1])):
            toR[math.floor(int(j)/int(w))][int(j) % int(w)] = 1
    return toR;

with open('stage1_train_labels.csv', newline='') as csvfile:
          datareader = csv.reader(csvfile, delimiter=' ', quotechar='|')
          #for row in datareader:
          next(datareader);
          row_1 = next(datareader)
          row_1[0] = row_1[0].split(',',1)[1]
          done = convertTo2D(256,256, row_1)
