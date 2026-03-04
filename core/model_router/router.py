class ModelRouter:
    """
    Select model based on task type.
    """
    
    def __init__(self, config):
        self.config = config

    def route(self, task_type):

        mapping = {
            "planning": "planner",
            "analysis": "reasoning",
            "coding": "coding",
            "summarize": "cheap"
        }

        model_key = mapping.get(task_type, "cheap")

        return self.config["models"][model_key]
