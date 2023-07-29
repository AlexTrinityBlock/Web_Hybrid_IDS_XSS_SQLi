import pandas as pd
import numpy as np
import re
from encode_utils import data2char_index,data_to_symbol_tag
import tflite_runtime.interpreter as tflite


text = '<script>123</script>'

input_text = data2char_index([text],max_len=1000)
input_symbol = data_to_symbol_tag([text],max_len=1000)

TFLITE_FILE_PATH = 'model.tflite'
# Load the TFLite model in TFLite Interpreter
interpreter = tflite.Interpreter(TFLITE_FILE_PATH)
interpreter.allocate_tensors()

# Get input and output tensors.
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# Test the model on random input data.
interpreter.set_tensor(input_details[0]['index'], [input_text])
interpreter.set_tensor(input_details[1]['index'], [input_symbol])

interpreter.invoke()

# The function `get_tensor()` returns a copy of the tensor data.
# Use `tensor()` in order to get a pointer to the tensor.
output_data = interpreter.get_tensor(output_details[0]['index'])
print(output_data)
