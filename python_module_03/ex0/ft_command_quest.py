import sys

if __name__ == "__main__":
    print("=== Command Quest ===")
    length: int = len(sys.argv)
    if length > 1:
        print(f"Arguments received: {length - 1}")
        index = 1
        while index < length:
            print(f"Argument {index}: {sys.argv[index]}")
            index += 1
        print(f"Total arguments: {length}")
    else:
        print("No arguments provided!")
        print(f"Program name: {sys.argv[0]}")
        print("Total arguments: 1")
