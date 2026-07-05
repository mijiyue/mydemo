from sort_test import bubble_sort, selection_sort, quick_sort


def main():
    data = [5, 3, 8, 4, 2]

    print("原始数据:", data)
    print("冒泡排序结果:", bubble_sort(data))
    print("快速排序结果:", quick_sort(data))


if __name__ == "__main__":
    main()