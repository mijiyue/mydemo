def bubble_sort(arr):
    """
    冒泡排序
    """
    nums = arr.copy()
    n = len(nums)

    for i in range(n):
        for j in range(0, n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]

    return nums


def selection_sort(arr):
    """
    选择排序
    """
    nums = arr.copy()
    n = len(nums)

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if nums[j] < nums[min_index]:
                min_index = j

        nums[i], nums[min_index] = nums[min_index], nums[i]

    return nums

def quick_sort(arr):
    """
    快速排序
    """
    nums = arr.copy()

    if len(nums) <= 1:
        return nums

    pivot = nums[0]
    left = [x for x in nums[1:] if x <= pivot]
    right = [x for x in nums[1:] if x > pivot]

    return quick_sort(left) + [pivot] + quick_sort(right)