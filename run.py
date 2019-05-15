import os
import numpy as np
import tensorflow as tf
import pandas as pd

train = pd.read_csv('../input/emnist-balanced-train.csv', header=None)
test = pd.read_csv('../input/emnist-balanced-test.csv', header=None)
train.head()
# class Pipeline:
#
#     def __init__(self, train, test):
#         self.train = train
#         self.test = test
#
#     def input(self):
#         """
#         Takes in input and puts it in a format ready for PCA and neural net
#         """
#         trainpath = os.path.join('./input', self.train)
#         testpath = os.path.join('./input', self.test)
#         filenames = [testpath]
#
#         record_defaults = [tf.float32] * 8
#         dataset = tf.contrib.data.CsvDataset(filenames, record_defaults)
#
#         # df_test = pd.read_csv(testpath)
#         # df_train = pd.read_csv(trainpath)
#
#         #print(list(df_test.columns.values))
#
# pipeline = Pipeline('emnist-letters-train.csv', 'emnist-letters-test.csv')
# pipeline.input()
