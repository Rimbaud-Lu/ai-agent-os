AGENTS = {}

def register(name, agent):
    AGENTS[name] = agent

def get(name):
    return AGENTS.get(name)
