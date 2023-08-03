import os
import openai
from prompts.analysis_prompt import get_prompt, get_system_prompt
from config import GPT_MODEL_NAME


class LogAnalysisController:
    def __init__(self):
        openai.api_key = os.getenv("OPENAI_API_KEY")
        dir_path = os.path.dirname(os.path.realpath(__file__))
        self.cache_text_path = dir_path + '/../analysis_cache/analysis_cache.txt'

    def message(self):
        return [
            {
                "role": "system",
                "content": get_system_prompt()
            },
            {
                "role": "user",
                "content": get_prompt()
            }
        ]

    def saving_cache(self, analysis_text):
        with open(self.cache_text_path, "w") as file:
            file.write(analysis_text)

    def gpt_analysis(self) -> str:
        response = openai.ChatCompletion.create(
            model=GPT_MODEL_NAME,
            messages=self.message(),
            temperature=0,
            max_tokens=2000,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        string_result = response["choices"][0]["message"]["content"]
        self.saving_cache(string_result)
        return {
            "result": string_result
        }

    def get_analysis_cache(self) -> str:
        string_result: str = ''
        with open(self.cache_text_path, "r") as file:
            string_result = file.read()
        return {
            "result": string_result
        }
