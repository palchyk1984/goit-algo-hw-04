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

def measure_sorting_time(func, size):
    data = [random.randint(0, 10000) for _ in range(size)]
    start_time = timeit.default_timer()
    func(data)
    return timeit.default_timer() - start_time

sizes = [100, 1000, 10000, 15000, 30000]  # Розміри наборів даних для тестування

# Зберігання результатів тестування
results = {"Insertion Sort": [], "Merge Sort": [], "Timsort": []}

for size in sizes:
    ins_sort_time = measure_sorting_time(insertion_sort, size)
    merge_sort_time = measure_sorting_time(merge_sort, size)
    timsort_time = measure_sorting_time(sorted, size)
    
    results["Insertion Sort"].append((size, ins_sort_time))
    results["Merge Sort"].append((size, merge_sort_time))
    results["Timsort"].append((size, timsort_time))

# Виведення результатів
for algorithm, timings in results.items():
    print(f"{algorithm}:")
    for size, time in timings:
        print(f"Size {size}: {time} seconds")
