'''
This Program creates a model using sequential api

Here we are using CNN of 3 layers (excluding the input layer)

filter size of 3x3 and input shape of 250x250x3 and output shape of 250x250x3

uses relu as Activation and mse as loss
'''

from pathlib import Path
from keras.models import Sequential
from keras.layers import Conv2D, BatchNormalization, Activation
from tensorflow.keras.optimizers import Adam

current_dir = Path(__file__).parent
model_path = current_dir / '../../Models/Model_1.01.h5'
model_path = model_path.resolve()

model = Sequential()

model.add(Conv2D(64, (3, 3), padding='same', input_shape=(250, 250, 3)))
model.add(BatchNormalization())
model.add(Activation('relu'))

model.add(Conv2D(64, (3, 3), padding='same'))
model.add(BatchNormalization())
model.add(Activation('relu'))

model.add(Conv2D(3, (3, 3), padding='same'))
model.add(Activation('sigmoid'))

model.compile(optimizer=Adam(), loss='mean_squared_error')

model.save(model_path)
            
            