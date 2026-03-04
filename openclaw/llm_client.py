from openclaw.model_router import get_model
from openclaw.plugin_loader import get_provider

def call_llm(task,prompt):

    provider_name,model = get_model(task)
    provider = get_provider(provider_name)

    return provider.generate(model,prompt)
