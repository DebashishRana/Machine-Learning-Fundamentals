import numpy as np


class Support_Vector_Machine:
    def __init__(self, learning_rate=0.001, epochs=1000, lambda_param=0.01):
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.lambda_param = lambda_param
        self.weights = None
        self.bias = 0.00

    # initializing the variables
    def initialize_weights(self, n_features: int) -> None:
        if n_features <= 0:
            raise ValueError("The number of features cannot be zero or negatives! Please enter correct Values ")
        self.weights = np.zeros(n_features, dtype=float)
        self.bias = 0


def fit(self, x, y):
    n_samples, n_features = x.shape
    y_ = np.where(y <= 0, 1 - 1)
    self.initialize_weights(n_)

    for epoch in range(self.epochs):
        for i, xi in enumerate(X):
    # margin check
