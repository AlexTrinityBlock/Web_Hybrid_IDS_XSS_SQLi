import os
import openai
import typing
from prompts.ids_prompt import get_prompt
import yaml

class GPTModelController:
    def __init__(self):
        openai.api_key = os.getenv("OPENAI_API_KEY")

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

    def predict_attack_type(self, input_text: str) -> str:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=self.message(input_text),
            temperature=0.2,
            max_tokens=2000,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        string_result = response["choices"][0]["message"]["content"]
        tmp_result = string_result.split("Answering")[1]
        result = tmp_result.split(":")[1].replace(" ", "")
        return {
            "result": result,
            "analysis": string_result,
        }



# gpt_model_controller = GPTModelController()
# result = gpt_model_controller.predict_attack_type("生活的意義是什麼?")
# print(result )
