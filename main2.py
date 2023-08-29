def bubble_sort(array):
    for i in range(len(array) - 1):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]


def main():
    array = [10, 8, 2, 4, 6, 7, 5, 9]
    print("Unsorted array:", array)
    bubble_sort(array)
    print("Sorted array:", array)


if __name__ == "__main__":
    main()
