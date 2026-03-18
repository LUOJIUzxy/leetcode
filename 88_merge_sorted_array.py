from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = m - 1
        j = n - 1
        k = m + n - 1

        while i >= 0 and j >= 0:
            if nums1[i] >= nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

          # 如果 nums2 还有剩余，说明 nums1 已经全部放完了，直接把 nums2 的剩余部分复制到 nums1 前面即可
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1