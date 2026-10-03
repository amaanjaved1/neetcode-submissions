class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # dictionary = {
        #     key (number itself): value (index in nums)
        # }

        mappings = {}

        # Populate mappings
        for index, num in enumerate(nums):
            if num in mappings:
                mappings[num].append(index)
            else:
                mappings[num] = [index]

        # Try to find and return the correct combo
        for index, num in enumerate(nums):
            difference_needed = target - num

            if difference_needed not in mappings:
                continue

            indexes_of_difference_needed = mappings[difference_needed]

            for index_of_difference_needed in indexes_of_difference_needed:
                if index_of_difference_needed != index:
                    return [index, index_of_difference_needed]
            