class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        write = n + m - 1
        read1 = m - 1
        read2 = n - 1

        while read1 >= 0 and read2 >= 0:
            if nums1[read1] >= nums2[read2]:
                nums1[write] = nums1[read1]
                read1 -= 1
            else:
                nums1[write] = nums2[read2]
                read2 -= 1
            write -= 1

        if read1 < 0:
            while read2 >= 0:
                nums1[write] = nums2[read2]
                read2 -= 1
                write -= 1