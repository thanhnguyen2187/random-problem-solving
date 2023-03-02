package take_home_01

// You are given a sorted array consisting of only integers where every element appears exactly twice, except for one
// element which appears exactly once.
//
// Return the single element that appears only once.
//
// Your solution must run in O(log n) time and O(1) space.

// FindSingleElement solves the problem by a simple intuition: there always is an odd amount of elements, so we can:
//
// - Split the elements to half
//
// - Make sure that the two half does not accidentally split a pair of same numbers
//
// - Return result of the half that is having an odd amount of elements
//
// For example:
//
//   Input: [0 0 1 1 2 3 3]
//   Split 1: [0 0 1 1]; Split 2: [2 3 3]
//   [0 0 1 1] is obviously not the one that we want, so we calculate the result from [2 3 3] and return 2 as the
//   answer.
//
func FindSingleElement(elements []int) int {
	n := len(elements)
	if n == 1 {
		return elements[0]
	}
	if n == 3 {
		if elements[0] == elements[1] {
			return elements[2]
		} else {
			return elements[0]
		}
	}

	// TODO: optimize for space by setting 3 variables,
	//       as recursive function calls also take space
	middleIndex := n / 2
	previousElement := elements[middleIndex-1]
	middleElement := elements[middleIndex]

	if previousElement == middleElement {
		leftHalf := elements[:middleIndex+1]
		rightHalf := elements[middleIndex+1:]
		if len(leftHalf)%2 == 1 {
			return FindSingleElement(leftHalf)
		} else {
			return FindSingleElement(rightHalf)
		}
	} else {
		leftHalf := elements[:middleIndex]
		rightHalf := elements[middleIndex:]
		if len(leftHalf)%2 == 1 {
			return FindSingleElement(leftHalf)
		} else {
			return FindSingleElement(rightHalf)
		}
	}
}
