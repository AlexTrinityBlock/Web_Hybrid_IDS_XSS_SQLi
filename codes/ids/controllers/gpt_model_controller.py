import os
import openai
import typing
from prompts.ids_prompt import get_prompt
import yaml
from config import GPT_MODEL_NAME


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
        tmp_result = string_result.split("Answering")[1]
        result = tmp_result.split(":")[1].replace(" ", "")
        return {
            "result": result,
            "message": string_result,
            "model": GPT_MODEL_NAME
        }
