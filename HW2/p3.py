import keras
from keras.datasets import cifar10
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras.datasets import cifar10
from tensorflow.keras.utils import to_categorical
from keras.layers import BatchNormalization
from keras.layers import Dropout
import os

#Loading the Data and print the output
(x_train, y_train), (x_test, y_test) = cifar10.load_data()
print('x_train shape:', x_train.shape)
print(x_train.shape[0], 'train samples')
print(x_test.shape[0], 'test samples')


#Choose 10% as the training data
x_train = x_train[0:5000,:]
y_train = y_train[0:5000,:]
x_test=x_test[0:1000,:]
y_test=y_test[0:1000,:]

#Normalize x training and testing data
#x_train, x_test = x_train/255.0, x_test/255.0

#change y train and test to categorical values with 10 classes
# NumOfClasses=10
# y_train = to_categorical(y_train, NumOfClasses)
# y_test= to_categorical(y_test,NumOfClasses)

y_train = keras.utils.to_categorical(y_train)
y_test = keras.utils.to_categorical(y_test)


# Create the first model with the layers below
# Add Convolution Layer -->  MaxPooling Layer -->  Convolution Layer -->  Flattern Layer -->  Dense layer (relu)-->  Dense Layer(softmax)
model = Sequential()
model.add(Conv2D(32, kernel_size=(5, 5), strides=(1, 1),
                 activation='relu',
                 input_shape=(32, 32, 3)))
model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))
model.add(Conv2D(64, (5, 5), activation='relu'))
model.add(Flatten())
model.add(Dense(1000, activation='relu'))
model.add(Dense(10, activation='softmax'))
model.compile(loss=keras.losses.categorical_crossentropy,
              optimizer=keras.optimizers.Adam(),
              metrics=['accuracy'])
print(model.summary())

#Fit the first model
history = model.fit(x_train, y_train, epochs=10, validation_split= 0.33,validation_data=(x_test,y_test), batch_size=128)

#Generate the plot for first model
import matplotlib.pyplot as plt
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper right')
plt.savefig('problem3_model_1.pdf')
plt.show()

##############################################################################################################################

# Create the second Model with batchnormalization layer
# Add Convolution Layer --> Batch Normalization Layer --> MaxPooling Layer -->  Convolution Layer -->  Flattern Layer -->  Dense layer (relu)-->  Dense Layer(softmax)
model_batch = Sequential()
model_batch.add(Conv2D(32, kernel_size=(5, 5), strides=(1, 1),
                 activation='relu',
                 input_shape=(32, 32, 3)))
model_batch.add(BatchNormalization())
model_batch.add(MaxPooling2D(pool_size=(2, 2)))
model_batch.add(Conv2D(64, (3, 3),strides=(2, 2),activation='relu'))
model_batch.add(Flatten())
model_batch.add(Dense(1000, activation='relu'))
model_batch.add(Dense(10, activation='softmax'))
model_batch.compile(loss=keras.losses.categorical_crossentropy,
              optimizer=keras.optimizers.Adam(),
              metrics=['accuracy'])
print(model_batch.summary())


#fit the second model with batch normalization
history_batch = model_batch.fit(x_train, y_train, epochs=10, validation_split= 0.33,validation_data=(x_test,y_test), batch_size=128)


#print the plot for the second model 
plt.plot(history_batch.history['loss'])
plt.plot(history_batch.history['val_loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper right')
plt.savefig('problem3_model_batch.pdf')
plt.show()
##############################################################################################################################



#Create the third model with dropout layer
model_dropout = Sequential()
model_dropout.add(Conv2D(32, kernel_size=(5, 5), strides=(1, 1),
                 activation='relu',
                 input_shape=(32, 32, 3)))
model_dropout.add(Dropout(0.15))
model_dropout.add(MaxPooling2D(pool_size=(2, 2)))
model_dropout.add(Conv2D(64, (3, 3),strides=(2, 2),activation='relu'))
model_dropout.add(Flatten())
model_dropout.add(Dense(1000, activation='relu'))
model_dropout.add(Dense(10, activation='softmax'))
model_dropout.compile(loss=keras.losses.categorical_crossentropy,
              optimizer=keras.optimizers.Adam(),
              metrics=['accuracy'])
print(model_dropout.summary())


#Fit the model with dropout layer
history_dropout = model_dropout.fit(x_train, y_train, epochs=10, validation_split= 0.33,validation_data=(x_test,y_test), batch_size=128)

plt.plot(history_dropout.history['loss'])
plt.plot(history_dropout.history['val_loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper right')
plt.savefig('problem3_model_dropout.pdf')
plt.show()

