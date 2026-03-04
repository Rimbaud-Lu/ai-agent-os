class TokenMonitor:

    def __init__(self):

        self.total_tokens = 0

    def record(self, tokens):

        self.total_tokens += tokens

    def report(self):

        return self.total_tokens
