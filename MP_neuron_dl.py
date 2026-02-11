import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
def mp_neuron(inputs, threshold):
    return 1 if sum(inputs) > threshold else 0
np.random.seed(42)
n_samples = 500
age = np.random.randint(20, 60, n_samples)          
salary = np.random.randint(20000, 150000, n_samples) 
family = np.random.randint(1, 7, n_samples)
X = np.column_stack((age, salary, family))
true_threshold = 100000
y = np.array([1 if sum(x) > true_threshold else 0 for x in X])
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)
train_sums = np.sum(X_train, axis=1)
threshold = train_sums[y_train == 1].mean()
y_pred = [mp_neuron(x, threshold) for x in X_test]
accuracy = accuracy_score(y_test, y_pred)
print("Threshold used:", threshold)
print("Test Accuracy:", accuracy)