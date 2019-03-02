import gameAI
import tensorflow as tf
import math


model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Dense(256, input_shape=[8]))
model.add(tf.keras.layers.Dense(512, input_shape=[256]))
model.add(tf.keras.layers.Dense(256, input_shape=[512]))
model.add(tf.keras.layers.Dense(2, input_shape=[256]))

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])


class AI:
    def __init__(self):
        self.previous_data = None
        self.training_data = [[], [], []]
        self.last_data_object = None
        self.turn = 0
        self.grab_data = True

    def save_data(self, bird, pipe):
        if not self.grab_data:
            return

        if not self.previous_data:
            data = [bird.y, pipe.x, pipe.top, pipe.bottom]
            self.previous_data = data

        data_xs = [bird.y, pipe.x, pipe.top, pipe.bottom]
        if bird.x < self.previous_data[0]:
            index = 0
        elif bird.x == self.previous_data[0]:
            index = 1
        else:
            index = 2

        self.last_data_object = [*self.previous_data, *data_xs]
        self.training_data[index].append(self.last_data_object)
        self.previous_data = data_xs

    def train(self):
        lenlist = [len(self.training_data[0]), len(self.training_data[1]), len(self.training_data[2])]
        length = min(lenlist)
        if not length:
            print("nothing to train")
            return

        data_xs = []
        data_xy = []
        for i in range(3):
            data_xs.append(slice(*self.training_data[i][:length]))
            if i == 0:
                data_xy.append()
