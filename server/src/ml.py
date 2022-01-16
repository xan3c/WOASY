import tensorflow as tf
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import Dense, Dropout, BatchNormalization
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import TensorBoard
import numpy as np 
import time

# Check for TensorFlow GPU access
print(f"TensorFlow has access to the following devices:\n{tf.config.list_physical_devices()}")

# See TensorFlow version
print(f"TensorFlow version: {tf.__version__}")

LOG_NAME = "test {}".format(int(time.time()))
tensorboard = TensorBoard(log_dir='logs/{}'.format(LOG_NAME))

MODEL_NAME = 'test.h5'
isLoad = False

array_length = 40 
n_classes = 2


''' DATA HANDLING
x = np.array([[1, 0, 1, 0.6],
              [0, 1, 1, 0.2],
              [1, 1, 0, 0.7],
              [0, 0, 1, 0.4],
              [1, 0, 1, 0.9],
              [0, 1, 1, 0.1],
              [1, 1, 0, 0.5],
              [0, 0, 1, 0.8]])

y = np.array([[0, 1],
              [1, 0],
              [1, 0],
              [1, 0],
              [0, 1],
              [0, 1],
              [1, 0],
              [0, 1]])

x_test = np.array([[0, 0, 1, 0.7],
                   [0, 1, 1, 0.3],
                   [1, 0, 1, 0.5],
                   [0, 1, 1, 0.9]])

y_test = np.array([[0, 1],
                   [1, 0],
                   [0, 1],
                   [0, 1]])
'''

if isLoad:
    model = load_model(MODEL_NAME)

else:
    model = Sequential()
    model.add(BatchNormalization())
    model.add(Dense(256, activation='relu'))
    model.add(BatchNormalization())
    model.add(Dense(100, activation='relu'))
    model.add(Dropout(0.5))
    model.add(BatchNormalization())
    model.add(Dense(n_classes, activation='softmax'))
    model.compile(optimizer=Adam(learning_rate=0.01), loss='binary_crossentropy', metrics=['accuracy'])

    model.fit(x, y, batch_size=256, epochs=50, shuffle=True, validation_data=(x_test, y_test), callbacks = [tensorboard])

    model.save(MODEL_NAME)

print(model.predict(x_test))
