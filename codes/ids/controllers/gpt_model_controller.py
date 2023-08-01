import os
import openai
import typing
from prompts.ids_prompt import get_prompt
import yaml
from config import GPT_MODEL_NAME
from controllers.log_controller import LogController  # Import LogController


class GPTModelController:
    def __init__(self):
        openai.api_key = os.getenv("OPENAI_API_KEY")
        self.log_controller = LogController()  # Initialize LogController

    def message(self, input_text: str):
        return [
            {
                "role": "system",
                "content": ""
            },
            {
                "role": "user",
                "content": get_prompt(input_text)
            }
        ]

    def predict_attack_type(self, input_text: str, from_ip: str) -> str:
        response = openai.ChatCompletion.create(
            model=GPT_MODEL_NAME,
            messages=self.message(input_text),
            temperature=0,
            max_tokens=2000,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        string_result = response["choices"][0]["message"]["content"]
        print("GPT raw response: ", string_result)
        try:
            tmp_result = string_result.split("Answering")[1]
            result = tmp_result.split(":")[1].replace(" ", "")
            # Get result string
            result_bool: bool = None
            if result == "True":
                result_bool = True
            elif result == "False":
                result_bool = False
            # Log
            self.log_controller.create_log(
                model_type=GPT_MODEL_NAME,
                result=result,
                payload=input_text,
                raw_gpt_response=string_result,
                is_positive=result_bool,
                from_ip=from_ip
            )
            return {
                "result": result,
                "message": string_result,
                "model": GPT_MODEL_NAME
            }

        except Exception as e:
            print(f"Error parsing GPT response: {e}")
            # Log
            self.log_controller.create_log(
                model_type=GPT_MODEL_NAME,
                result="Unknown",
                payload=input_text,
                raw_gpt_response=string_result
            )
            return {
                "result": "Unknown",
                "message": f"Unable to parse the GPT response.",
                "raw_gpt_response": string_result,
                "model": GPT_MODEL_NAME
            }
