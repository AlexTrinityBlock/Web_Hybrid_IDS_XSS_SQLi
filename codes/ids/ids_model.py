from encode_utils import data2char_index, data_to_symbol_tag
import tensorflow as tf
from tensorflow import keras


class IDSModel:
    def __init__(self) -> None:
        self.model = keras.models.load_model("./model.h5", compile=False)

    def predict(self, text: str) -> dict:

        input_text = data2char_index([text], max_len=1000)
        input_symbol = data_to_symbol_tag([text], max_len=1000)
        pred = self.model.predict([input_text, input_symbol])
        softmax_result = tf.nn.softmax(pred[0])
        result = {
            "SQLi": round(float(softmax_result[0]),3),
            "XSS": round(float(softmax_result[1]),3),
            "Benign": round(float(softmax_result[2]),3)                                     
        }
        return result
