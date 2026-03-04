import yaml

def load():
    with open("config/models.yaml") as f:
        return yaml.safe_load(f)
