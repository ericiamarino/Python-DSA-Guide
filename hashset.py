# Hashsets, similar to their counterpart hashmaps (dictionaries) in Python, are essential data structures
# that shine when it comes to efficiently managing collections of unique elements. The key strength of a
# hashset lies in its ability to provide fast insertion, containment checks, and removal of elements,
# exhibiting an amortized time complexity of O(1). Though collisions can potentially lead to
# a less favorable worst-case time complexity, the probability of encountering such situations remains low,
# allowing hashsets to maintain their predominant efficiency.

# Beyond their remarkable time complexity, hashsets offer additional noteworthy features. Their constant-time
# performance for fundamental operations like adding and checking the existence of elements makes them a
# preferred choice across diverse programming scenarios. It's vital to note that hashsets, much like hashmaps,
# do not impose any specific ordering on elements, setting them apart from structures like lists or arrays.
# This unordered characteristic should be kept in mind while working with hashsets. Furthermore, the underlying
# hash functions that govern element storage and retrieval play a pivotal role. A well-designed hash function
# can effectively mitigate collision issues, thereby enhancing the overall efficiency of hashset operations.

# In the context of coding interviews and platforms like LeetCode, hashsets prove to be invaluable tools for
# solving a range of problems. They find particular utility in scenarios involving deduplication, frequency
# counting, and rapid data retrieval. Many algorithmic challenges leverage hashsets to optimize solutions,
# especially in situations where the focus is on efficiently tracking unique elements or swiftly storing
# and retrieving information.

def main():
    # Creating a hashset
    my_hashset = set()

    # Adding elements to the hashset
    my_hashset.add("Element 1")
    my_hashset.add("Element 2")
    my_hashset.add("Element 3")

    # Checking if an element is in the hashset
    if "Element 1" in my_hashset:
        print("Element 1 is in the hashset.")
    else:
        print("Element 1 is not in the hashset.")

    if "Element 4" in my_hashset:
        print("Element 4 is in the hashset.")
    else:
        print("Element 4 is not in the hashset.")

    # Removing elements from the hashset
    my_hashset.remove("Element 3")

    # Printing the hashset
    print("Current hashset:", my_hashset)


if __name__ == "__main__":
    main()
