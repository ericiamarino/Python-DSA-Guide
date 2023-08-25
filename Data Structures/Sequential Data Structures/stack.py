def main():
    # Creating a stack
    stack = []

    # Push elements onto the stack
    stack.append('a')
    stack.append('b')
    stack.append('c')

    # Showcasing Elements
    print(stack)

    # Pop elements from stack in LIFO order
    print('\nElements popped from stack in order')
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())

    # New Stack size
    print('New Stack Size: ', len(stack))

if __name__ == "__main__":
    main()