import math

# A direct approach to compute the discrete cosine transform
# of a finite complex sequence z

# Time complexity O(n^2)

def DCT_II_brute (z):
	L = len(z)
	R = range(L)
	w = [0 for i in R]
	Z = [[0] * L for i in R]

	for n in R:
		for m in R:
			arg = math.pi * (n + 0.5) * m / L
			Z[n][m] = z[n] * math.cos(arg)
		w[n] = sum(Z[n])
	return w
