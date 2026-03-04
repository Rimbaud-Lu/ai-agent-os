class AgentEventBus:

    def __init__(self):

        self.subscribers = {}

    def subscribe(self, agent_name, handler):

        self.subscribers[agent_name] = handler

    def publish(self, receiver, message):

        if receiver in self.subscribers:

            self.subscribers[receiver](message)
