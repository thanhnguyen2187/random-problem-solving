package take_home_01

import (
	"testing"
)

func TestFindSingleElement(t *testing.T) {
	inputs := [][]int{
		{0},
		{0, 1, 1},
		{0, 0, 1},
		{0, 0, 1, 1, 2, 2, 3},
		{0, 1, 1, 2, 2, 3, 3, 4, 4},
		{0, 0, 1, 1, 2, 2, 3, 3, 4, 5, 5},
		{0, 0, 1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6},
		{0, 0, 1, 2, 2},
	}
	expectedAnswers := []int{
		0,
		0,
		1,
		3,
		0,
		4,
		4,
		1,
	}
	answers := make([]int, 0)
	for _, input := range inputs {
		answers = append(answers, FindSingleElement(input))
	}

	for i := range inputs {
		input := inputs[i]
		answer := answers[i]
		expectedAnswer := expectedAnswers[i]
		if answer != expectedAnswer {
			t.Errorf("input %v; expected %v; got %v", input, expectedAnswer, answer)
		}
	}
}
