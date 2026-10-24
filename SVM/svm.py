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

    def fit(self, X, y):
        n_samples, n_features = X.shape
        y_ = np.where(y <= 0, -1, 1)
        self.initialize_weights(n_features)

        for epoch in range(self.epochs):
            for i in range(n_samples):
                score = X[i] @ self.weights + self.bias

                if y_[i] * score >= 1:
                    self.weights = self.weights - self.learning_rate * self.lambda_param * self.weights
                else:
                    self.weights = self.weights - self.learning_rate * (self.lambda_param * self.weights - y_[i] * X[i])
                    self.bias = self.bias + self.learning_rate * y_[i]

    def predict(self, X):
        return np.sign(X @ self.weights + self.bias)