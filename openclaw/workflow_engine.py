class WorkflowEngine:

    def __init__(self, planner, agents):

        self.planner = planner
        self.agents = agents


    def run(self, task):

        print("Planning phase...")

        plan = self.planner.plan(task)

        print("Execution phase...")

        result = self.execute_agents(plan)

        print("Testing phase...")

        self.test(result)

        print("Review phase...")

        self.review(result)

        print("Deployment phase...")

        self.deploy(result)


    def execute_agents(self, plan):

        outputs = []

        for step in plan["tasks"]:

            for agent in self.agents:

                if agent.can_handle(step):

                    outputs.append(agent.run(step))


        return outputs


    def test(self, code):

        print("Running tests")


    def review(self, code):

        print("Reviewing code")


    def deploy(self, code):

        print("Deploying application")
