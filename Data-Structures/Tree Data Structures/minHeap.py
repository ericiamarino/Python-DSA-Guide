import heapq

def main():
    # Instantiate min_heap
    min_heap = []

    # Use heapq package to insert into minheap
    heapq.heappush(min_heap, 5)
    heapq.heappush(min_heap, 3)
    heapq.heappush(min_heap, 8)
    heapq.heappush(min_heap, 1)
    heapq.heappush(min_heap, 10)

    # Peak at top of heap
    print("Top of Heap: ", min_heap[0])

    # Pop element at top of heap
    print("Smallest Element: ", heapq.heappop(min_heap))

    # Convert a list into a min-heap in place
    heapq.heapify(min_heap)
    print("Min-Heap", min_heap)


if __name__ == "__main__":
     main()