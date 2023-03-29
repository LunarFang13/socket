from sklearn.datasets import load_digits
import numpy as np

digits = load_digits()

x = np.array(digits.data)
# x = x/255
x = x.T

y = np.array(digits.target).T

def relu(z):
    return np.maximum(z,0)

def d_relu(z):
    return z>0

def sigmoid(z):
    return 1/(1+np.exp(-z))

w1 = np.random.rand(10,64) - 0.5
w2 = np.random.rand(10,10) - 0.5
b1 = np.random.rand(10, 1) - 0.5
b2 = np.random.rand(10, 1) - 0.5

lr = 0.01

m = 1797

def one_hot(Y):
    one_hot_Y = np.zeros((Y.size, Y.max() + 1))
    one_hot_Y[np.arange(Y.size), Y] = 1
    one_hot_Y = one_hot_Y.T

    return one_hot_Y

for i in range(10000):
    
    z1 = np.dot(w1,x) + b1
    a1 = relu(z1)
    z2 = np.dot(w2,a1) + b2
    a2 = sigmoid(z2)
    
    one_hot_Y = one_hot(y)

    dz2 = a2 - one_hot_Y
    dw2 = np.dot(dz2,a1.T)/m
    db2 = np.sum(dz2, axis=1, keepdims=True)/m
    dz1 = np.dot(w2.T,dz2) * d_relu(z1)
    dw1 = np.dot(dz1,x.T)/m
    db1 = np.sum(dz1, axis=1, keepdims=True)

    w1 = w1 - lr*dw1
    b1 = b1 - lr*db1
    w2 = w2 - lr*dw2
    b2 = b2 - lr*db2
    print(i)



z1 = np.dot(w1,x) + b1
a1 = relu(z1)
z2 = np.dot(w2,a1) + b2
a2 = sigmoid(z2)


def get_predictions(A2):
    return np.argmax(A2, 0)
    

print(get_predictions(a2))
print(y)