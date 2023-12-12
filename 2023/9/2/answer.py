import numpy as np
from numpy.polynomial import Polynomial as P


def main():
    extrapolated_sum = 0
    with open("input.txt") as f:
        for line in f:
            sequence = np.asarray([int(x) for x in line.strip().split()])
            ind = np.arange(sequence.shape[0])
            p = P.fit(ind, sequence, sequence.shape[0] - 1).convert()
            extrapolated_sum += int(np.rint(p(-1)))

    print(extrapolated_sum)


if __name__ == "__main__":
    main()
