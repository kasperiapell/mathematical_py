"""
Y is an N x 1 vector of 'responses'
B is an 1 x M vector of parameters 
X is a M x K matrix of '' ('design matrix')
E is an N x 1 vector of errors

Given these, we have the multiple linear regression equation
Y = BX + E

Let || denote the N-dimensional euclidean norm. In OLS, we are minimising the loss function
B -> |Y - X B|^2

Given that X is nonsingular, this admits a unique solution given by
\hat{B} := (X^T X)^{-1} X^T Y
"""

import numpy as np

def OLS(X, Y):
	Xt = X.transpose()
	Z = np.linalg.inv(Xt @ X)
	return Z @ Xt @ Y