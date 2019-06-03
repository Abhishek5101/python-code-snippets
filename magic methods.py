class Letter:
    def __init__(self, pattern=None):
        self.pattern = pattern

    def __str__(self):
        morse = []
        for i in self.pattern:
            if i == "."
                morse.append("Dot")
            elif i == "_":
                morse.append("Dash")
        return "-".join(morse)

class S(Letter):
    def __init__(self):
        pattern = ['.', '.', '.']
        super().__init__(pattern)