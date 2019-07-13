class Hand(list):
    def __init__(self, size=0, die_class=None, *args, **kwargs):
        if not die_class:
            raise ValueError("Must provide class")
        super().__init__()

        for _ in range(size):
            self.append(die_class())
