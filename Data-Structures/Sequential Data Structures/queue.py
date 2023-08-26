# A Queue is a sequential data structure which follows the FIFO principle. This principle, first in first out,
# has the logic that the first element added will be at the front of the queue. A way to visualize a
# queue can be by imagining a line at a restaurant or a music queue - The first elements queued up will be the
# first ones served or heard.

# The benefits of a queue are that the insertion and removal times are constant O(1). Elements of a queue
# are added enqueued, and when you dequeue or view the top of the queue, it will be the first added item.
# One of the downsides of this however is that searching for an item in a queue will be O(n). Additionally
# There is no random access in most queue implementations.

# Queue are a pretty prominent data structure used throughout leetcode. The largest use cases are typically
# for implementing algorithms. Additionaly a queue is the data structure used to implement the breadth-first-search
# algorithm.

def main():
    # Creating a queue
    queue = []

    # Push elements onto the queue
    queue.append('a')
    queue.append('b')
    queue.append('c')

    # Showcasing Elements
    print(queue)

    # Pop elements from stack in FIFO order
    print('\nElements popped from queue in order')
    print(queue.pop(0))
    print(queue.pop(0))
    print(queue.pop(0))

    # New Stack size
    print('New Queue Size: ', len(queue))

if __name__ == "__main__":
    main()