package mathmath

var bigOne uint64 = 1

// Factorial function.
func Factorial(n uint64) uint64 {
	if n == 0 {
		return bigOne
	}
	return n * Factorial(n-bigOne)
}

// Catalan number
// https://en.wikipedia.org/wiki/Catalan_number
func CatalanNumber(n uint64) (t uint64) {
	twoN := 2 * n
	t = Factorial(twoN) / (Factorial(n+bigOne) * Factorial(n))
	return
}
