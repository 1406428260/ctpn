import numpy as np
mu=1
sigma = 0.1
data = np.random.normal(loc=mu, scale=sigma, size=100)
v = mu
beta = 0.9
# 我设置这个序列都是1
for d in range(10):
	v = beta * v + (1-beta)/10 * d
print(v)