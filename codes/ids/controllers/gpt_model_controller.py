import os
import openai
import typing
from prompts.ids_prompt import get_prompt

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
                "content": get_prompt() + input_text
            }
        ]

    def genarate_detection(self, input_text: str) -> str:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=self.message(input_text),
            temperature=0,
            max_tokens=2000,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        return response["choices"][0]["message"]["content"]


gpt_model_controller = GPTModelController()
result = gpt_model_controller.genarate_detection("生活的意義是什麼?")
print(result )
