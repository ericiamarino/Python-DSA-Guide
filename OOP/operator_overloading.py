
class Bank:
    def __init__(self, dollars=0, quarters=0, pennies=0):
        self.dollars = dollars
        self.quarters = quarters
        self.pennies = pennies

    def __str__(self):
        return f"{self.dollars} Dollars, {self.quarters} Quarters, {self.pennies} Pennies"

    # Operator overloading to add two objects values
    def __add__(self, other):
        dollars = self.dollars + other.dollars
        quarters = self.quarters + other.quarters
        pennies = self.pennies + other.pennies

        return Bank(dollars, quarters, pennies)



def main():
    Eric = Bank(20000,10,5)
    Slinky = Bank(5, 5, 5)

    # Adding two objects
    total = Eric + Slinky

    # Print three different objects now
    print(Eric)
    print(Slinky)
    print(total)


if __name__ == "__main__":
    main()