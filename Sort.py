# def quicksort(A, start, end):

#     if start >= end: return

#     left, right = start, end

#     pivot = A[(start + end) // 2]

#     while left <= right:

#         while left <= right and A[left] < pivot: left += 1
#         while left <= right and A[right] > pivot: right -= 1
#         if left <= right:
#             A[left], A[right] = A[right], A[left]

#             left += 1
#             right -= 1
    
#     quicksort(A, start, right)
#     quicksort(A, left, end)

# def sortIn(A):

#     quicksort(A, 0, len(A)-1)

#     return A

# a = [3, 5, 4 ,6]
# a = sortIn(a)
# print(a)

# def merge(nums, l, m, r):

#     n1 = m - l + 1
#     n2 = r - m

#     # create tmp
#     L = [0] * n1
#     R = [0] * n2

#     # copy
#     for i in range(n1):
#         L[i] = nums[l+i]

#     for i in range(n2):
#         R[i] = nums[m+1+i]

#     i, j = 0, 0
#     k = l

#     while i < n1 and j < n2:

#         if L[i] < R[j]:
#             nums[k] = L[i]
#             i += 1
#         else:
#             nums[k] = R[j]
#             j += 1
        
#         k += 1

#     while i < n1:
#         nums[k] = L[i]
#         i += 1
#         k += 1

#     while j < n2:
#         nums[k] = R[j]
#         j += 1
#         k += 1

# def mergeSort(nums, l, r):

#     if l < r:

#         m = (l + r) // 2
#         mergeSort(nums, l, m)
#         mergeSort(nums, m+1, r)
#         merge(nums, l, m, r)

# nums = [12, 11, 13, 5, 6, 7]
# mergeSort(nums, 0, len(nums)-1)
# print(nums)

        
# def insertSort(nums):

#     for i in range(1, len(nums)):

#         key = nums[i]

#         j = i-1

#         while j >= 0 and key < nums[j]: 
#             nums[j+1] = nums[j]
#             j -= 1

#         nums[j+1] = key

#     return nums

# nums = [12, 11, 13, 5, 6, 7]
# nums = insertSort(nums)
# print(nums)

def mergeSort(nums):
    pass

def merge(nums1, nums2):

    out = []

    i, j = 0, 0

    while i < len(nums1) and j < len(nums2):

        if nums1[i] > nums2[j]:

            out.append(nums2[j])
            j += 1

        else:

            out.append(nums1[i])
            i += 1

    while i < len(nums1):

        out.append(nums1[i])
        i += 1

    while j < len(nums2):

        out.append(nums2[j])
        j += 1

    return out

def mergeSort(nums):

    if nums == []:

        return

    if len(nums) == 1:

        return [nums[0]]
    
    m = (len(nums)) // 2

    out1, out2 = mergeSort(nums[:m]), mergeSort(nums[m:])

    return merge(out1, out2)

nums = [12, 11, 13, 5, 6, 7]

res = mergeSort(nums)
print(res)