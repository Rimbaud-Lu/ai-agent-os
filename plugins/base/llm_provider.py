class LLMProvider:

    def __init__(self, config):
        self.config = config

    def generate(self, model, prompt):
        raise NotImplementedError
