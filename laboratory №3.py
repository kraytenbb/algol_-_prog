import time
import matplotlib.pyplot as plt
import random


def measure_time(func, data):
    start = time.perf_counter()
    func(data.copy())
    end = time.perf_counter()
    return end - start


def radix_sort(arr):
    if len(arr) == 0:
        return arr
    max_val = max(arr)
    exp = 1
    while max_val // exp > 0:
        arr = sort_by_digit(arr, exp)
        exp *= 10
    return arr


def sort_by_digit(arr, exp):
    buckets = [[] for _ in range(10)]
    for num in arr:
        digit = (num // exp) % 10
        buckets[digit].append(num)
    return concatenate_buckets(buckets)


def concatenate_buckets(buckets):
    result = []
    for bucket in buckets:
        result.extend(bucket)
    return result


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[-1]
    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)


sizes = [100, 500, 1000, 2000, 5000]
times_radix = []
times_merge = []
times_quick = []

for size in sizes:
    arr = [random.randint(0, 10000) for _ in range(size)]
    times_radix.append(measure_time(radix_sort, arr))
    times_merge.append(measure_time(merge_sort, arr))
    times_quick.append(measure_time(quick_sort, arr))


print("Таблица замеров времени выполнения:")
print(f"{'Размер':<10} {'Radix Sort':<12} {'Merge Sort':<12} {'Quick Sort':<12}")
for i, size in enumerate(sizes):
    print(f"{size:<10} {times_radix[i]:<12.6f} {times_merge[i]:<12.6f} {times_quick[i]:<12.6f}")


plt.figure(figsize=(12, 7))
plt.plot(sizes, times_radix, label='Radix Sort', color='blue')
plt.plot(sizes, times_merge, label='Merge Sort', color='green')
plt.plot(sizes, times_quick, label='Quick Sort', color='red')

plt.title('Сравнение времени выполнения алгоритмов сортировки')
plt.xlabel('Количество элементов в массиве')
plt.ylabel('Время выполнения алгоритма, с')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
