import requests
from plugins.base.llm_provider import LLMProvider

class OpenAIProvider(LLMProvider):

    def generate(self, model, prompt):

        r = requests.post(
            f"{self.config['base_url']}/chat/completions",
            headers={"Authorization":f"Bearer {self.config['api_key']}"},
            json={"model":model,"messages":[{"role":"user","content":prompt}]}
        )

        return r.json()
