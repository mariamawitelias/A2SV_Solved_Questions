class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = Counter(words)
        arr = []
        for word, freq in count.items():
            arr.append([-freq, word])
        heapify(arr)
        res = []
        for _ in range(k):
            freq, word = heappop(arr)
            res.append(word)
        return res