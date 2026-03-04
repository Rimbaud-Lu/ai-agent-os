from plugins.registry import PROVIDERS
from openclaw.config_loader import load

CONFIG = load()

def get_provider(name):

    provider = PROVIDERS[name]
    cfg = CONFIG["providers"][name]

    return provider(cfg)
