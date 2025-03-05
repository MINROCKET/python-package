import sys

from hexlet_python_package import half


def main():
    print(half(float(sys.argv[-1])))


if __name__ == "__main__":
    main()
