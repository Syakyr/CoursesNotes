import numpy as np
import pandas as pd

def get_data():
    df= pd.read_csv('ecommerce_data.csv')
    data = df.as_matrix()

    X = data[:, :-1] # Everything except user_action
    Y = data[:, -1]  # user_action data

    # Regularisation (Normalisation)
    X[:,1] = (X[:,1] - X[:,1].mean() / X[:,1].std())
    X[:,2] = (X[:,2] - X[:,2].mean() / X[:,1].std())

    # Accommodate the matrix to one-hot encoding for time_of_day
    N, D = X.shape # X is 500 * 5 matrix

    # Creates a zero matrix of size 500*8,
    # expand 3 more columns to accommodate
    # the 3 other choices of time_of_day
    X2 = np.zeros((N, D+3))
    X2[:,0:(D-1)] = X[:,0:(D-1)] # Copy the rest except time_of_day

    # # Method 1:
    # for n in range(N):
    #     t = int(X[n,D-1]) # Takes the value of time_of_day
    #     X2[n, t+D-1] = 1  # Set the value of 1 into respective columns

    # Method 2:
    Z = np.zeros((N, 4)) # Creates 500*4 matrix just for the encoding
    Z[np.arange(N), X[:,D-1].astype(np.int32)] = 1 # Uses time_of_day value to determine the placement of '1' into its respective columns
    X2[:,-4:] = Z # Slot Z back into the amended matrix
    assert(np.abs(X2[:,-4:] - Z).sum() < 10e-10) # Asserts that all Z values are copied properly, i.e. the sum is 0

    return X2, Y

# Filtering only 0 (bounce) and 1 (add_to_cart) for analysis
def get_binary_data():
    X, Y = get_data()
    X2 = X[Y <= 1]
    Y2 = Y[Y <= 1]
    return X2, Y2
