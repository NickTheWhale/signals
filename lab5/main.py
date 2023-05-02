import numpy as np
import time


W1, W2, W3 = 49, 400, 5500
# x = [a1, a2, a3]
# x = [ 0,  1,  2]
def gain(x, w0):
    A = (w0 * x[0]) / np.sqrt(W1*W1 + w0*w0)
    B = x[1] / np.sqrt(W2*W2 + w0*w0)
    C = x[2] / np.sqrt(W3*W3 + w0*w0)
    return A * B * C


def main():
    start = time.time()
    for i in range(100):
        for j in range(100):
            for k in range(100):
                gain([i, j, k], 1)
    stop = time.time()
    print(stop - start)


if __name__ == "__main__":
    main()
