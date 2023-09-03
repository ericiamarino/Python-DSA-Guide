# Immutable: Values that can't change in value  (Tuple is an example)
# Ex: return (name, house)

# Mutable: Can change the values of if  needed
# Ex: return [name, house]


# Example 1: Using Immutable tuple
def get_student():
    name = input("Name: ")
    house = input("House: ")
    return (name, house)

def main():
    student = get_student()
    print(f"{student[0]} from {student[1]}")



if __name__ == "__main__":
     main()