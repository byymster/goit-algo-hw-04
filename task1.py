import random
import timeit

# Реалізація сортування злиттям
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Реалізація сортування вставками
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Генерація випадкового списку
def generate_random_list(size):
    return [random.randint(0, 10000) for _ in range(size)]

# Порівняння часу виконання
def compare_sorting_algorithms():
    sizes = [1000, 5000, 10000]
    for size in sizes:
        arr = generate_random_list(size)

        # Копії для кожного алгоритму
        arr_merge = arr.copy()
        arr_insertion = arr.copy()
        arr_timsort = arr.copy()

        # Час для сортування злиттям
        merge_time = timeit.timeit(lambda: merge_sort(arr_merge), number=1)

        # Час для сортування вставками
        insertion_time = timeit.timeit(lambda: insertion_sort(arr_insertion), number=1)

        # Час для Timsort
        timsort_time = timeit.timeit(lambda: sorted(arr_timsort), number=1)

        print(f"Розмір масиву: {size}")
        print(f"Час сортування злиттям: {merge_time:.6f} сек")
        print(f"Час сортування вставками: {insertion_time:.6f} сек")
        print(f"Час Timsort: {timsort_time:.6f} сек")
        print("-" * 40)

if __name__ == "__main__":
    compare_sorting_algorithms()
