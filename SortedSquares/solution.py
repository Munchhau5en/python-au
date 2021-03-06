class Solution():

    def get_first_non_negative(self, nums):
        for i, val in enumerate(nums):
            if val >= 0:
                return i
        return len(nums)

    def sortedSquares(self, nums):
        right = self.get_first_non_negative(nums)
        left = right - 1
        result = []

        while left >= 0 and right < len(nums):
            if nums[left] ** 2 < nums[right] ** 2:
                result.append(nums[left] ** 2)
                left -= 1
            else:
                result.append(nums[right] ** 2)
                right += 1

        while left >= 0:
            result.append(nums[left] ** 2)
            left -= 1

        while right < len(nums):
            result.append(nums[right] ** 2)
            right += 1

        return result
