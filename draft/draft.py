from pathlib import Path
import os

if __name__ == "__main__":

    i: bool = os.access("data", os.W_OK)
    print(os.path.isfile("sqsq"))