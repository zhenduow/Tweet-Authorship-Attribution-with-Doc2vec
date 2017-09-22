from __future__ import print_function
import keras
import re
import numpy as np
from numpy import *
from matplotlib.mlab import PCA
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv1D, MaxPooling1D
from keras.utils import np_utils
from keras import backend as K
K.set_image_dim_ordering('th')

author_num = 1000
text_num = 200
feature_dim = 50
classification_dim=feature_dim
ker_num=64
ker_size=3
train_epoch=20
test_size = author_num * text_num / 5
train_size = 4 * test_size

vector_list_train = []
author_list_train = []
vector_list_test = []
author_list_test = []

doc_train = open('train.txt') 
lines = doc_train.readlines()
for l in lines:
	m = re.match('([^\s]+) (.+)', l)
	author = m.group(1)
	author_list_train.append(author)
	vector = m.group(2)
	vector = re.split(' ',vector)
	float_vector=[]
	for str in vector:
		k = re.match('(\d+)\:(.+)', str)
		strval = k.group(2)
		float_vector.append(float(strval))	
	vector_list_train.append(float_vector)
doc_train.close()

doc_test = open('group_5.txt') 
lines = doc_test.readlines()
for l in lines:
	m = re.match('([^\s]+) (.+)', l)
	author = m.group(1)
	author_list_test.append(author)
	vector = m.group(2)
	vector = re.split(' ',vector)
	float_vector=[]
	for str in vector:
		k = re.match('(\d+)\:(.+)', str)
		strval = k.group(2)
		float_vector.append(float(strval))	
	vector_list_test.append(float_vector)
doc_test.close()

X_train = np.array(vector_list_train)
y_train = np.array(author_list_train)
X_test = np.array(vector_list_test)
y_test = np.array(author_list_test)


#X = np.concatenate((X_train,X_test))
#X = mat(X)
#pca = PCA(X)
#fracs = pca.fracs
#print (fracs)
#X = np.array(pca.Y[:,:classification_dim])
#X_train = X[:train_size]
#X_test = X[train_size:]



Y_train = np_utils.to_categorical(y_train, author_num)
Y_test = np_utils.to_categorical(y_test, author_num)
X_train = X_train.reshape((train_size,classification_dim,1))
X_test = X_test.reshape((test_size,classification_dim,1))

model = Sequential()
model.add(Conv1D(2*ker_num, 2*ker_size, activation='relu',border_mode='same', input_shape=(classification_dim,1)))
model.add(MaxPooling1D(2))
#model.add(Conv1D(ker_num, ker_size, activation='relu',border_mode='same'))
#model.add(MaxPooling1D(3))
model.add(Dropout(0.5))
model.add(Flatten())
model.add(Dense(author_num, activation='softmax'))
model.summary()

model.compile(loss="categorical_crossentropy", optimizer="adam",metrics=['accuracy'])


model.fit(X_train, Y_train, nb_epoch=train_epoch, show_accuracy=True)

score = model.evaluate(X_test, Y_test, verbose=0)
print('Kernel number:',ker_num)
print('Kernel size:',ker_size)
print('Test loss:', score[0])
print('Test accuracy:', score[1])