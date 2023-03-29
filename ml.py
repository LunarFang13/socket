import numpy as np

def sigmoid(z):
    return 1/(1+np.exp(-z))

x = np.array([[0,0,1,1],[0,1,0,1]])
y = np.array([[0,1,1,0]])

w1 = np.random.randn(2,2)
w2 = np.random.randn(1,2)
b1 = np.zeros((2, 1))
b2 = np.zeros((1, 1))

m = x.shape[1]
lr = 0.01

for i in range(100000):
    z1 = np.dot(w1,x) + b1
    a1 = sigmoid(z1)

    z2 = np.dot(w2,a1) + b2
    a2 = sigmoid(z2)

    dz2 = a2 - y
    dw2 = np.dot(dz2,a1.T)/m
    db2 = np.sum(dz2,axis=1,keepdims=True)

    da1 = np.dot(w2.T,dz2)
    dz1 = np.multiply(da1, a1*(1-a1))
    dw1 = np.dot(dz1,x.T)/m
    db1 = np.sum(dz1,axis=1 , keepdims=True)

    w1 = w1 - lr*dw1
    b1 = b1 - lr*db1
    w2 = w2 - lr*dw2
    b2 = b2 - lr*db2

X = np.array([[1, 1, 0, 0], [0, 1, 0, 1]])


z1 = np.dot(w1,X) + b1
a1 = sigmoid(z1)
z2 = np.dot(w2,a1) + b2
a2 = sigmoid(z2)

print(a2)

