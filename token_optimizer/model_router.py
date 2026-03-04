class ModelRouter:

    MODEL_ROUTER = {
        "planning": "claude",
        "coding": "codex",
        "review": "deepseek",
        "compression": "qwen"
    }

    def route(self, task_type):

        return self.MODEL_ROUTER.get(task_type, "codex")
