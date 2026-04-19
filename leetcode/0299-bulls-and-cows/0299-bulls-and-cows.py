class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bull = 0
        for i in range(len(secret)):
            bull += int(secret[i] == guess[i])
        cows = 0
        for c in set(secret):
            cows += min(secret.count(c), guess.count(c))
        return f"{bull}A{cows-bull}B"