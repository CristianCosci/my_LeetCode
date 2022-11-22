class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m == 0:
            nums1[:] = nums2[:]
        elif n != 0:
            aux_list_nums1 = nums1[:m]
            count_1 = 0
            count_2 = 0
            for i in range(n+m):
                if aux_list_nums1[count_1] <= nums2[count_2]:
                    nums1[i] = aux_list_nums1[count_1]
                    count_1 += 1
                    if count_1 == m:
                        count_1 -= 1
                        aux_list_nums1[count_1] = inf
                elif count_2 < n:
                    nums1[i] = nums2[count_2]
                    count_2 += 1
                    if count_2 == n:
                        count_2 -= 1
                        nums2[count_2] = inf
                