# Hashmaps, also referred to as dictionaries in Python, are indispensable data structures that excel in
# facilitating efficient insertion, retrieval, and deletion operations for key-value pairs. The hallmark
# of a hashmap is its remarkable amortized time complexity of O(1) for most common operations. While it's
# true that collisions can lead to a worst-case scenario of O(n), the likelihood of this occurrence is
# quite low, ensuring the prevalent efficiency of O(1) on average.

# Beyond their impressive time complexity, hashmaps offer a few more important insights. First, they
# provide constant-time average-case performance for fundamental tasks like adding, accessing, and deleting
# elements, making them a go-to choice in various programming scenarios. Second, hashmaps don't guarantee
# any specific order of elements, unlike lists or arrays. This unordered nature is vital to remember when
# working with hashmaps. Lastly, hash functions, which determine the storage and retrieval of values, play
# a crucial role. A well-designed hash function can significantly minimize collisions and enhance overall
# hashmap efficiency.

# In the realm of coding interviews and platforms like LeetCode, hashmaps find widespread use in solving
# problems that involve deduplication, frequency counting, and quick data retrieval. Many algorithmic
# challenges require the use of hashmaps to optimize solutions, especially when dealing with scenarios
# where tracking unique elements or efficiently storing and looking up information is paramount.

def main():
    # Creating a hashmap
    my_hashmap = {}

    # Inserting into hashmap
    my_hashmap["Example 1"] = 1
    my_hashmap["Example 2"] = 2
    my_hashmap["Example 3"] = 3

    # Accessing hashmap
    print("Accessing Element 1: ", my_hashmap.get("Example 1"))
    print("Accessing Element 2: ", my_hashmap.get("Example 2"))
    print("Accessing Element 3: ", my_hashmap.get("Example 3"))

    # Deleting from hashmap
    del my_hashmap["Example 1"]
    del my_hashmap["Example 2"]

    # Searching in python
    if "Example 3" in my_hashmap:
        print("Found Element 3!")


if __name__ == "__main__":
    main()