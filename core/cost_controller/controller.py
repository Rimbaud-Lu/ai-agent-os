class CostController:
    """
    Control token usage and prevent runaway LLM calls.
    """

    def __init__(self):

        self.max_tokens_per_task = 4000
        self.max_agent_iterations = 8

    def check_tokens(self, tokens_used):

        if tokens_used > self.max_tokens_per_task:
            raise Exception("Token limit exceeded")

    def check_iterations(self, iteration):

        if iteration > self.max_agent_iterations:
            raise Exception("Agent iteration limit reached")
