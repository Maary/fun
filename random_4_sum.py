# python3.8

import random
from typing import List


class Solution:

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) == 0:
            return []
        seed = 1
        total = 10000
        res = []

        while seed < total:
            getter_1 = random.randint(0, len(nums)-1)
            getter_2 = random.randint(0, len(nums)-1)
            getter_3 = random.randint(0, len(nums)-1)
            getter_4 = random.randint(0, len(nums)-1)
            if nums[getter_1] + nums[getter_2] + nums[getter_3] + nums[getter_4] == target:
                if getter_1 != getter_2 and \
                        getter_1 != getter_3 and\
                        getter_1 != getter_4 and \
                        getter_2 != getter_3 and \
                        getter_2 != getter_4 and \
                        getter_3 != getter_4:
                    tem = [nums[getter_1], nums[getter_2], nums[getter_3], nums[getter_4]]
                    if len(res) == 0:
                        res.append(tem)
                        continue
                    ok = False
                    for i in range(0, len(res)):
                        if self.is_arr_equal(res[i], tem):
                            ok = True
                    if not ok:
                        res.append(tem)
            seed = seed + 1
        return res

    def is_arr_equal(self, arr_1, arr_2):
        if len(arr_1) != len(arr_2):
            return False
        arr_2 = sorted(arr_2)
        arr_1 = sorted(arr_1)
        for i in range(0,  len(arr_1)):
            if arr_1[i] != arr_2[i]:
                return False
        return True



sol = Solution()
res = sol.fourSum([1, 0, -1, 0, -2, 2], 0)
print(res)
# print(sol.is_arr_equal([-1, 0, 0, 1], [-1, 0, 1, 0]))
