import pandas as pd

red_wine = pd.read_csv('red-wine.csv')
print(red_wine.head())

rows, columns = red_wine.shape
print(f'The dataframe has {rows} rows and {columns} columns.')

# YOUR CODE HERE
input_shape = [11]

print(input_shape)

from tensorflow import keras
from tensorflow.keras import layers

# YOUR CODE HERE
model = keras.Sequential([
    layers.Dense(units=1, input_shape=[11])
])
print(model)

w, b = model.weights

print("Weights\n{}\n\nBias\n{}".format(w, b))
