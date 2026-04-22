class Solution:
    def twoEditWords(self, queries: list[str], dictionary: list[str]) -> list[str]:
        def within_two_edits(w1, w2):
            return sum(a != b for a, b in zip(w1, w2)) <= 2
        
        return [q for q in queries if any(within_two_edits(q, d) for d in dictionary)]