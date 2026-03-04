from runtime.agent_registry import get

def run_agent(name, task):

    agent = get(name)

    if not agent:
        return {"error":"agent not found"}

    return agent.run(task)
