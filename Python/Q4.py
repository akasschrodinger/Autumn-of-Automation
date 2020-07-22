import numpy as np

def prog():

	X= np.random.normal(size=(20,20))
	y= np.random.randint(1, 100, size=(20,1), dtype=np.int32)
	Xtrans= X.transpose()
	Xm= np.dot(X,Xtrans)
	Xm=np.linalg.inv(Xm)
	Xfinal= np.dot(Xm,Xtrans)

	return np.dot(Xfinal, y)

