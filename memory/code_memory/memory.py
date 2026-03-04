class CodeMemory:
    """
    Store reusable code patterns to reduce regeneration.
    """

    def __init__(self):

        self.patterns = {}

    def add_pattern(self, name, code):

        self.patterns[name] = code

    def get_pattern(self, name):

        return self.patterns.get(name)

    def list_patterns(self):

        return list(self.patterns.keys())
