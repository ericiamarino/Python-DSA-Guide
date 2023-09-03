# Example 3: Creating immutable object with properties - Instance variable/method
class Student:
    def __init__(self, name, major):
        self.name = name
        self.major = major

    @property
    def major(self):
        return self._major

    @major.setter
    def major(self, major):
        self._major = major

    # Getter - Gets the attribute
    @property
    def name(self):
        # Variable and function can't be "name" so use "_" in front of instance name
        return self._name

    # Setter - Sets the attribute
    @name.setter
    def name(self, name):
        if name not in ["Eric"]:
            raise ValueError("Invalid House")

        # Variable and function can't be "name" so use "_" in front of instance name
        self._name = name


def get_student():
    # Taking in attributes as input
    name = input("Name: ")
    major = input("Major: ")
    print()

    # Constructor Call to build student object
    return Student(name, major)

def main():
    student = get_student()

    print(f"{student.name} is studying {student.major}")

    try:
        student.name = "Changing name"
    except ValueError:
        print("Can't change name")



if __name__ == "__main__":
     main()