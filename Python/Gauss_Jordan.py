import numpy as np

def gauss_jordan(a, b):
    # Combine the coefficient matrix and the constant vector into one augmented matrix
    a = np.array(a, dtype=float)
    b = np.array(b, dtype=float).reshape(-1, 1)
    aug = np.hstack([a, b])
    n = len(aug)

    for i in range(n):
        # Make the pivot = 1
        aug[i] = aug[i] / aug[i][i]
        
        # Eliminate all other elements in that column
        for j in range(n):
            if i != j:
                factor = aug[j][i]
                aug[j] = aug[j] - factor * aug[i]

    # The last column now contains the solution
    return aug[:, -1]
