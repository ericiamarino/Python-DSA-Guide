# The list data structure in Python is a versatile container that can hold elements of different types.
# Think of it as a dynamic array that automatically resizes itself. Items are stored in a sequential
# manner, allowing easy access through indexing. Lists follow the concept of ordered collection, meaning
# elements retain their order, which can be useful for maintaining sequences of data.

# Lists offer several advantages, including constant-time (O(1)) access and modification of elements by index.
# Appending elements to the end is also efficient, usually taking O(1) time. However, inserting or deleting
# elements in the middle or at the beginning can be slow, especially for larger lists (O(n) time). Lists are
# mutable, so you can change their contents after creation. Keep in mind that due to their dynamic resizing,
# they may consume more memory than other data structures for small-sized collections.

# In the world of LeetCode and coding challenges, lists shine in various scenarios. They're perfect for tasks
# that involve manipulating arrays, such as two-pointer techniques, sliding windows, and array transformations.
# Lists can simulate queues and stacks for solving problems related to breadth-first search (BFS) or depth-first
# search (DFS). When optimized, lists are efficient for dynamic programming tasks, helping to store and manage
# intermediate results. However, for more specialized use cases with specific requirements, other data structures
# like heaps or hashmaps might offer better performance.


def main():
    # Creating a list
    string_array = []

    # Inserting into list
    string_array.append("String 1")
    string_array.append("String 2")
    string_array.append("String 3")

    # Accessing hashmap
    for i in range(len(string_array)):
        print("Element", i, ": ", string_array[i])

    # Deleting from list
    string_array.remove("String 1")

    # Searching in python
    print("Element 0: ", string_array[0])


if __name__ == "__main__":
    main()