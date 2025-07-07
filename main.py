import sys


def main():
    pattern, filename = sys.argv[1:]
    with open(filename) as file:
        for line in file:
            if pattern in line:
                print(line.strip())


if __name__ == "__main__":
    main()
