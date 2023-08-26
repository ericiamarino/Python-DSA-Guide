import heapq

def main():
    # Instantiate min_heap
    max_heap = []

    # Use heapq package to insert into minheap
    heapq.heappush(max_heap, 5)
    heapq.heappush(max_heap, 3)
    heapq.heappush(max_heap, 8)
    heapq.heappush(max_heap, 1)
    heapq.heappush(max_heap, 10)

    heapq._heapify_max(max_heap)

    # Peak at top of heap
    print("Top of Heap: ", max_heap[0])

    # Pop element at top of heap
    print("Smallest Element: ", heapq.heappop(max_heap))

    # Convert a list into a min-heap in place
    print("Min-Heap", max_heap)


if __name__ == "__main__":
     main()