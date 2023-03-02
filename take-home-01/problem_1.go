package take_home_01

import (
	"math"
)

// Problem: Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go
// outside the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0.
//
// Note: Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
//
// CheckOverflow functions source: https://stackoverflow.com/questions/199333/how-do-i-detect-unsigned-integer-overflow

func CheckOverflowAdd(x int32, y int32) bool {
	return (x > 0 && x > math.MaxInt32-y) || // x + y can overflow
		(x < 0 && x < math.MinInt32-y) //       x + y can underflow
}

func CheckOverflowMultiply(x int32, y int32) bool {
	// TODO: check a bug where both x = -1 and y = -1 return wrong result
	return (x == -1 && y == math.MinInt32) || // x * y can overflow
		(y == -1 && x == math.MinInt32) || //    x * y can overflow
		(x != 0 && y > math.MaxInt32/x) || //    x * y can overflow
		(x != 0 && y < math.MinInt32/x) //       x * y can underflow
}

func Reverse(x int32) int32 {
	result := int32(0)
	signed := x < 0
	if signed {
		if CheckOverflowMultiply(x, -1) {
			return 0
		}
		x *= -1
	}
	for x > 0 {
		if CheckOverflowMultiply(result, 10) {
			return 0
		}
		result *= 10
		if CheckOverflowAdd(result, x%10) {
			return 0
		}
		result += x % 10
		x /= 10
	}
	if CheckOverflowAdd(result, x) {
		return 0
	}
	result += x

	if signed {
		if CheckOverflowMultiply(result, -1) {
			return 0
		}
		result *= -1
	}
	return result
}
