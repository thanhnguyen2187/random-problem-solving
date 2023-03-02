package take_home_01

// Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod
// operator.
//
// The integer division should truncate toward zero, which means losing its fractional part. For example, 8.345 would be
// truncated to 8, and -2.7335 would be truncated to -2.
//
// Return the quotient after dividing dividend by divisor.
//
// Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer
// range: [−2^31, 2^31 − 1]. For this problem, if the quotient is strictly greater than 2^31 - 1, then return 2^31 - 1,
// and if the quotient is strictly less than -2^31 , then return -2^31.

func Abs(x int32) int32 {
	if x > 0 {
		return x
	} else {
		return -x
	}
}

func DivideWithoutOperators(dividend int32, divisor int32) int32 {
	if divisor == 0 {
		panic("DivideWithoutOperators divides by zero")
	}

	signed := (dividend > 0 && divisor < 0) ||
		(dividend < 0 && divisor > 0)
	dividend = Abs(dividend)
	divisor = Abs(divisor)

	if (dividend == 0) || (dividend < divisor) {
		return 0
	}
	if divisor == 1 {
		if !signed {
			return dividend
		} else {
			return -dividend
		}
	}

	quotient := int32(0)
	temp := int32(0)
	for temp <= dividend {
		quotient += 1
		temp += divisor
	}
	quotient -= 1

	if !signed {
		return quotient
	} else {
		return -quotient
	}
}
