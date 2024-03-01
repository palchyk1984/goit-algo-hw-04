import timeit
import random

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def measure_time(func, arr):
    start_time = timeit.default_timer()
    func(arr.copy())
    return timeit.default_timer() - start_time

# Генерація випадкового масиву даних
array_size = 10000
data = [random.randint(0, 10000) for _ in range(array_size)]

# Вимірювання та вивід часу виконання
insertion_sort_time = measure_time(insertion_sort, data)
merge_sort_time = measure_time(merge_sort, data)
timsort_time = measure_time(sorted, data)

print(f"Insertion Sort: {insertion_sort_time} seconds")
print(f"Merge Sort: {merge_sort_time} seconds")
print(f"Timsort: {timsort_time} seconds")
