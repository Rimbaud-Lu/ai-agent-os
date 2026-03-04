class AgentLifecycle:

    def start(self, agent):

        print(f"Starting agent {agent}")

    def stop(self, agent):

        print(f"Stopping agent {agent}")

    def restart(self, agent):

        self.stop(agent)
        self.start(agent)
