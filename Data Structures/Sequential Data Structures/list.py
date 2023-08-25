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