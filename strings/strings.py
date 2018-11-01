import data


class Strings:

    def __init__(self):
        print(
            """
            String Problems
            1.winner of election
            2.Maximum length of consecutive 1in a binary string
            """
        )

    def electionWinner(self, votes=data.electionWinner_Votes):
        candidates = {}
        for c in votes:
            if candidates.has_key(c):
                candidates[c] = candidates[c] + 1
            else:
                candidates[c] = 1
        winnder = max(candidates.items(), key=lambda x: x[1])
        print('winner is {0} with votes {1}'.format(winnder[0], winnder[1]))

    def maxBinaryOnes(self, data=data.maxBinaryOnes_str):
        print(max(map(len, data.split('0'))))


s=Strings()
s.maxBinaryOnes()
