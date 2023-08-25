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