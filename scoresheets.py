
class YatzyScoresheet:
    @staticmethod
    def score_ones(hand):
        return sum(hand.ones)

    @staticmethod
    def score_twos(hand):
        return sum(hand.twos)

    @staticmethod
    def score_threes(hand):
        return sum(hand.threes)

    @staticmethod
    def score_fours(hand):
        return sum(hand.fours)

    @staticmethod
    def score_fives(hand):
        return sum(hand.fives)

    @staticmethod
    def score_sixes(hand):
        return sum(hand.sixes)

    def _score_set(self, hand, set_size):
        scores = []
        for worth, count in hand._sets.items():
            scores.append(worth*set_size)
        return sum(scores)

