# !/usr/local/bin/python
import sugartensor as tf
import numpy as np
import util
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
os.environ["CUDA_VISIBLE_DEVICES"] = '0'

config=tf.ConfigProto()
config.gpu_options.per_process_gpu_memory_fraction = 0.7 # maximun alloc gpu50% of MEM
config.gpu_options.allow_growth = True #allocate dynamically

# PARAMS #
num_layers = 3
activation = tf.nn.relu
batchsize = 8
w_dropout = 0.4
path_to_train_data = "__data/stage1_train"
path_to_test_data = "__data/stage1_test"

img_dat = util.crawl_path(path_to_train_data)

graph = tf.Graph()
with graph.as_default():
    #batchsize*x_max*y_max*rgb(3)
    features = tf.placeholder(tf.float32,[None,None,None,3])
    labels = tf.placeholder(tf.int32,[None,None])
    input_layer = tf.reshape(features, [-1, 2048, 2048, 3])
    training = tf.placeholder(tf.bool)


    conv1 = tf.layers.conv2d(
        inputs=input_layer,
        filters=32,
        kernel_size=[11, 11],
        padding="same",
        activation=tf.nn.relu)
    print('conv1',conv1.get_shape())
    pool1 = tf.layers.max_pooling2d(inputs=conv1, pool_size=[4, 4], strides=2)
    print('pool1',pool1.get_shape())
    conv2 = tf.layers.conv2d(
        inputs=input_layer,
        filters=64,
        kernel_size=[5, 5],
        padding="same",
        activation=tf.nn.relu)
    print('conv2',conv2.get_shape())
    pool2 = tf.layers.max_pooling2d(inputs=conv1, pool_size=[4, 4], strides=2)
    print('pool2',pool2.get_shape())
    conv3 = tf.layers.conv2d(
        inputs=input_layer,
        filters=128,
        kernel_size=[3, 3],
        padding="same",
        activation=tf.nn.relu)
    print('conv3',conv3.get_shape())
    pool3 = tf.layers.max_pooling2d(inputs=conv1, pool_size=[4, 4], strides=2)
    print('pool3',pool3.get_shape())
    pool4_flat = tf.reshape(pool2, [-1, 32 * 32 * 128])
    dense = tf.layers.dense(inputs=pool4_flat, units=4096, activation=tf.nn.relu)
    dropout = tf.layers.dropout(inputs=dense, rate=w_dropout, training=training)
