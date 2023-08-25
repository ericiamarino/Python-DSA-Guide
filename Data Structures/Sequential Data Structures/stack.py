# A Stack is a sequential data structure which follows the LIFO principle. This principle, last in first out,
# has the logic that the most recently added element will be at the top of the stack. A way to visualize a
# stack can be as a stack of dishes or stack of towels - the last one placed is at the top and is the one
# you'd grab.

# The benefits of a stack are that the insertion and removal times are constant O(1). Elements of a stack
# are added to the top, and when you remove or view the top of the stack, it will be the last added item.
# One of the downsides of this however is that searching for an item in a stack will be O(n). Additionally
# There is no random acess in most stack implementations.

# Stacks are a pretty prominent data structure used throughout leetcode. The largest use cases are typically
# for valid anagram and valid parantheses. Typicaly when you want to compare the first half of something
# to the second half. Additionaly a stack is the data structure used to implement the Depth-first-search
# and topological sorting algorithms.

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