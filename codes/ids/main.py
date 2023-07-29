import pandas as pd
import numpy as np
import re
from encode_utils import data2char_index,data_to_symbol_tag
import tensorflow as tf
from tensorflow import keras

model = keras.models.load_model("./model.h5", compile=False)


text = 'Peter Or ally'
input_text = data2char_index([text],max_len=1000)
input_symbol = data_to_symbol_tag([text],max_len=1000)

pred = model.predict([input_text,input_symbol])

sf = tf.nn.softmax(pred[0])

print(sf)