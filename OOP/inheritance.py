# Inheritance: Defining multiple classes that are somewhat related to one another

class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("Missing Name")
        self.name = name


class Student(Wizard):
    def __init__(self, name, house):
        # Accessing super or parent class it inherits
        super().__init__(name)

        self.house = house


class Professor(Wizard):
    def __init__(self, name, subject):
        # Accessing super or parent class it inherits
        super().__init__(name)

        self.subject = subject

def main():
    wizard = Wizard("Wizard_Rando")
    student = Student("Harry", "HouseName")
    professor = Professor("Severus", "Course taught")


if __name__ == "__main__":
    main()
