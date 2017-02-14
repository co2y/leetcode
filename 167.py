class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = 0
        right = len(numbers) - 1
        while left < right:
            if numbers[left] + numbers[right] == target:
                break

            if numbers[left] + numbers[right] < target:
                left += 1
            else:
                right -= 1

        return [left + 1, right + 1]
