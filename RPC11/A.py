N, K = map(int, input().split())

def f(x):
	if x <= K:
		return x
	return f(x // (K + 1)),  x % (K + 1)

print(f(N))

#001001 1 111