from utils.encode_utils import data2char_index, data_to_symbol_tag
import tensorflow as tf
from tensorflow import keras
import os
from config import ATTACK_THRESHOLD, BENIGN_THRESHOLD, LOCAL_MODEL_NAME
from controllers.gpt_model_controller import GPTModelController


class LocalModelController:
    def __init__(self, model: keras.Model) -> None:
        self.model = model
        self.gpt_model_controller = GPTModelController()

    def predict_attack_type(self, text: str) -> dict:
        input_text = data2char_index([text], max_len=1000)
        input_symbol = data_to_symbol_tag([text], max_len=1000)
        pred = self.model.predict([input_text, input_symbol])
        softmax_result = tf.nn.softmax(pred[0])

        # Probability
        SQLi_probability: float = round(float(softmax_result[0]), 3)
        XSS_probability: float = round(float(softmax_result[1]), 3)
        Benign_probability: float = round(float(softmax_result[2]), 3)

        # Result
        result_bool: bool = False

        # If Benign_probability is less than 0.33, then we will consider the result is under attack.
        if Benign_probability < 0.33:
            result_bool = True

        # If the local model can provide the result, then we will use the local model.
        result = {
            "result": str(result_bool),
            "message": "Analyzing through a local model.",
            "model": LOCAL_MODEL_NAME,
            "SQLi": SQLi_probability,
            "XSS": XSS_probability,
            "Benign": Benign_probability
        }

        return result
