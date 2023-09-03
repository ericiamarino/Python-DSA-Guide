# Example 2: Using classes to create objects
# Classes are mutable by nature but can be made immutable

class Student:
    # Instance Method to initialize contents of a method
    def __init__(self, name, major, grade=None):
        # Raise error if name is null or major invalid
        if not name:
            raise ValueError("Missing name")
        if major not in ["Computer Engineering", "Computer Science", "Test Major"]:
            raise ValueError("Invalid major")
        self.name = name
        self.major = major

        # Optional attribute
        self.grade = grade

    # Showing the object as a string
    def __str__(self):
        return f"{self.name} student Object"

    # Method within a class
    def grade_earned(self):
        if self.grade == "A" or self.grade == "B" or self.grade == "C":
            return "Passing"
        else:
            return "Failing"

    # Class method
    @classmethod
    def get(cls):
        name = input("Name: ")
        major = input("Major: ")
        grade = input("Grade: ")
        return cls(name, major, grade)

def main():
    # Constructing student object
    student_a = Student.get()
    student_b = Student.get()

    # Accessing attributes of an object
    print(f"{student_a.name} is studying {student_a.major}")
    print(f"{student_b.name} is studying {student_b.major}")

    # Printing the object itself - Prints location in memory without __str__ method
    print(student_a)
    print(student_b)

    # Using methods within the class
    print(student_a.grade_earned())
    print(student_b.grade_earned())

    # Mutable DS Exemplified
    student_b.name = "New Name"
    print(student_b.name)


if __name__ == "__main__":
     main()