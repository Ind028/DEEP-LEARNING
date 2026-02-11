import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
def perceptron(inputs, weights):
    weighted_sum = np.dot(inputs, weights)
    if weighted_sum > 0:
        return 1
    else:
        return 0
np.random.seed(42)
n_samples = 500
age = np.random.randint(20, 60, n_samples)
salary = np.random.randint(20000, 150000, n_samples)
family = np.random.randint(1, 7, n_samples)
X = np.column_stack((age, salary, family))
true_weights = np.array([0.02, 0.00001, 0.5])
y = np.array([1 if np.dot(x, true_weights) > 0 else 0 for x in X])
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)
weights = np.array([0.02, 0.00001, 0.5])
y_pred = [perceptron(x, weights) for x in X_test]
accuracy = accuracy_score(y_test, y_pred)
print("Weights used:", weights)
print("Test Accuracy:", accuracy)