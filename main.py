import sys
from src.controller.EdgeDetector import EdgeDetector


def catch_exceptions(t, val, tb):
    print(format(t))
    old_hook(t, val, tb)


old_hook = sys.excepthook
sys.excepthook = catch_exceptions


def main():
    EdgeDetector()

if __name__ == "__main__":
    main()
