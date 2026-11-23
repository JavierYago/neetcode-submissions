class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        repetido = set()
        for n in nums:
            if n in repetido:
                return True
            repetido.add(n)
        return False