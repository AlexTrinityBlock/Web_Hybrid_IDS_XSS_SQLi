from utils.encode_utils import data2char_index, data_to_symbol_tag
import tensorflow as tf
from tensorflow import keras
import os
from config import THRESHOLD
from controllers.gpt_model_controller import GPTModelController


class IDSModelController:
    def __init__(self) -> None:
        dir_path = os.path.dirname(os.path.realpath(__file__))
        self.model = keras.models.load_model(
            dir_path+"/../ml_models/model.h5")
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

        # If the local model can not sure the result, then we will use the GPT model.
        if Benign_probability < THRESHOLD:
            result_gpt = self.gpt_model_controller.predict_attack_type(
                text)
            return result_gpt
        
        # If the local model can provide the result, then we will use the local model.
        if Benign_probability < 0.33:
            result_bool = True

        result = {
            "result": str(result_bool),
            "Message": "Analyzing through a local model.",
            "SQLi": SQLi_probability,
            "XSS": XSS_probability,
            "Benign": Benign_probability
        }
        
        return result
