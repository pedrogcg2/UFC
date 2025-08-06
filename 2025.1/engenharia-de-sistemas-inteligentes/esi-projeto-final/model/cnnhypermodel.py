import keras_tuner as kt
from tensorflow.keras import optimizers
from tensorflow.keras.layers import Input, Flatten, Dense, Conv2D, MaxPooling2D, Rescaling, RandomFlip, RandomRotation, RandomTranslation
from tensorflow.keras.models import Sequential

class CNNHyperModel(kt.HyperModel):
    def __init__(self, num_classes, input_shape):
        self.num_classes = num_classes
        self.input_shape = input_shape

    def build(self, hp):
        model = Sequential()
        model.add(Input(shape=self.input_shape))
        model.add(Rescaling(1./255))

        model.add(RandomFlip("horizontal_and_vertical"))
        model.add(RandomRotation(0.1))
        model.add(RandomTranslation(height_factor=0.1, width_factor=0.1))

        hp_filters_first_conv = hp.Choice('first_conv', values=[16,32])
        hp_filters_second_conv = hp.Choice('second_conv', values=[32, 64])
        hp_filters_third_conv = hp.Choice('third_conv', values=[64, 128])
       
        model.add(Conv2D(hp_filters_first_conv, (3, 3), activation='relu'))
        model.add(MaxPooling2D(2, 2))

        model.add(Conv2D(hp_filters_second_conv, (3, 3), activation='relu'))
        model.add(MaxPooling2D(2, 2))
        
        model.add(Conv2D(hp_filters_third_conv, (3, 3), activation='relu'))
        model.add(MaxPooling2D(2, 2))

        model.add(Flatten(name='flatten'))

        hp_units = hp.Int('units', min_value=128, max_value=512, step=128)
        model.add(Dense(units=hp_units, activation='relu'))
        model.add(Dense(self.num_classes, activation='softmax'))
        hp_learning_rate = hp.Float('learning_rate', min_value=1e-4, max_value=1e-2, sampling='log')

        model.compile(optimizers.Adam(learning_rate=hp_learning_rate),
                      loss='sparse_categorical_crossentropy',
                      metrics=['accuracy'])

        return model

