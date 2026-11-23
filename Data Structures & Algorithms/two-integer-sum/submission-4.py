class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numeros = {}
        for indice,n in enumerate(nums):
            falta = target -n
            if falta in numeros:
                return [numeros[falta], indice]
            numeros[n] = indice
