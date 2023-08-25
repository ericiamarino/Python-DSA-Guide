
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