class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frecuency = {}
        result = []
        for n in nums:
            if n in frecuency:
                frecuency[n] +=1
            else:
                frecuency[n] = 1
        order = sorted(frecuency.keys(), key=frecuency.get, reverse=True)

        for i in range(k):
            result.append(order[i])
        return result