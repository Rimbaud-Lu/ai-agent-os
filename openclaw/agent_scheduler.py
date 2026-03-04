class AgentScheduler:

    def __init__(self, agents):

        self.agents = agents


    def schedule(self, task):

        for agent in self.agents:

            if agent.can_handle(task):

                return agent

        return None
