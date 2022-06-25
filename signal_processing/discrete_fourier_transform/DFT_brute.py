import math

# A direct approach to compute the discrete Fourier transform
# of a finite complex sequence z

# Time complexity O(n^2)

def DFT_brute (z):
	L = len(z)
	R = range(L)
	w = [0 for i in R]
	Z = [[0] * L for i in R]

	for n in R:
		for m in R:
			arg = (2 * math.pi * n * m) / L
			Z[n][m] = z[n] * (math.cos(arg) - complex(0, math.sin(arg)))
		w[n] = sum(Z[n])
	return w
