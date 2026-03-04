class ControlPlane:

    def __init__(self, workflow_engine):

        self.workflow_engine = workflow_engine

    def run(self, task):

        return self.workflow_engine.run(task)
