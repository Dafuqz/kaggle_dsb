# !/usr/local/bin/python
import sugartensor as tf
import numpy as np
import util

# PARAMS #
num_layers = 3
activation = tf.nn.relu
batchsize = 8
path_to_train_data = "__data/stage1_train"
path_to_test_data = "__data/stage1_test"

img_dat = util.crawl_path(path_to_train_data)


def cnn(features,labels):
 input_layer = tf.reshape(features, [-1, 28, 3])
