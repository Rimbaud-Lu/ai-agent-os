import hashlib

class PromptCache:
    """
    Cache identical prompts to reduce token usage.
    """

    def __init__(self):

        self.cache = {}

    def _hash(self, prompt):

        return hashlib.sha256(prompt.encode()).hexdigest()

    def get(self, prompt):

        key = self._hash(prompt)

        return self.cache.get(key)

    def set(self, prompt, response):

        key = self._hash(prompt)

        self.cache[key] = response
