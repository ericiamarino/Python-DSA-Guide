import argparse

# Command line script: python etc.py -f Eric -l Iamarino
def main():
    parser = argparse.ArgumentParser(description="Program Description")

    parser.add_argument("-f", default=1, help="Enter first name", type=str)
    parser.add_argument("-l", default=1, help="Enter last name", type=str)

    args = parser.parse_args()

    print(f"Hello {args.f} {args.l}")

if __name__ == "__main__":
    main()