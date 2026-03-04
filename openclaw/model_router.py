from openclaw.config_loader import load

CONFIG = load()

def get_model(task):
    m = CONFIG["models"][task]
    return m["provider"], m["model"]
