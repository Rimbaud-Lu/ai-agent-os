class PromptCompressor:

    def compress(self, prompt):

        if len(prompt) > 2000:
            return prompt[:2000]

        return prompt
