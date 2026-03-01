import threading
import random
import time
import matplotlib.pyplot as plt

def quick_sort_sequential(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort_sequential(left) + middle + quick_sort_sequential(right)

def sort_chunk(arr, start, end, result, index):
    chunk = arr[start:end]
    sorted_chunk = quick_sort_sequential(chunk)
    result[index] = sorted_chunk

def merge_two_arrays(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result

def merge_all_chunks(chunks):
    while len(chunks) > 1:
        new_chunks = []
        for i in range(0, len(chunks), 2):
            if i + 1 < len(chunks):
                merged = merge_two_arrays(chunks[i], chunks[i + 1])
                new_chunks.append(merged)
            else:
                new_chunks.append(chunks[i])
        chunks = new_chunks

    return chunks[0] if chunks else []

def parallel_quick_sort(arr, num_threads):
    n = len(arr)
    if n == 0:
        return []

    chunk_size = n // num_threads
    threads = []
    result = [None] * num_threads

    for i in range(num_threads):
        start = i * chunk_size
        if i != num_threads - 1:
            end = (i + 1) * chunk_size
        else:
            end = n

        thread = threading.Thread(
            target=sort_chunk,
            args=(arr, start, end, result, i)
        )
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    sorted_array = merge_all_chunks(result)

    return sorted_array

def sequential_quick_sort(arr):
    return quick_sort_sequential(arr)

def measure_time(sort_func, arr, num_threads=None):
    arr_copy = arr.copy()

    start = time.time()
    if num_threads:
        result = sort_func(arr_copy, num_threads)
    else:
        result = sort_func(arr_copy)
    end = time.time()

    return end - start, result

if __name__ == '__main__':

    sizes = [10000, 50000, 100000, 250000, 500000, 750000, 1000000]

    thread_configs = [
        {"name": "1 поток", "threads": 1, "color": "red"},
        {"name": "2 потока", "threads": 2, "color": "blue"},
        {"name": "4 потока", "threads": 4, "color": "green"},
        {"name": "8 потоков", "threads": 8, "color": "purple"},
    ]

    results = {cfg["name"]: [] for cfg in thread_configs}

    print(f"{'Элементов':>12} {'1 поток':>14} {'2 потока':>14} "
          f"{'4 потока':>14} {'8 потоков':>14}")

    for size in sizes:
        arr = [random.randint(0, 10_000_000) for _ in range(size)]
        row_times = []

        for cfg in thread_configs:
            num_threads = cfg["threads"]

            if num_threads == 1:
                t, sorted_result = measure_time(sequential_quick_sort, arr)
            else:
                t, sorted_result = measure_time(parallel_quick_sort, arr, num_threads)

            results[cfg["name"]].append(t)
            row_times.append(t)

        print(f"{size:>12,} {row_times[0]:>14.6f} {row_times[1]:>14.6f} "
              f"{row_times[2]:>14.6f} {row_times[3]:>14.6f}")
    plt.figure(figsize=(12, 7))
    for cfg in thread_configs:
        plt.plot(sizes, results[cfg["name"]], color=cfg["color"],
                 linewidth=2.5, markersize=10, label=cfg["name"])

    plt.xlabel('Количество элементов', fontsize=14)
    plt.ylabel('Время (секунды)', fontsize=14)
    plt.title('Время выполнения быстрой сортировки', fontsize=16)
    plt.legend(fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.xticks(sizes, [f'{s // 1000}K' for s in sizes], rotation=45)
    plt.tight_layout()
    plt.show()
  
