package take_home_01

import (
	"testing"
)

func TestDivideWithoutOperators(t *testing.T) {
	inputs := [][]int32{
		{0, 1},
		{1, 2},
		{2, 2},
		{9, 2},
		{9, -1},
		{9, -2},
	}
	expectedAnswers := []int32{
		0,
		0,
		1,
		4,
		-9,
		-4,
	}
	answers := make([]int32, 0)
	for _, input := range inputs {
		answers = append(answers, DivideWithoutOperators(input[0], input[1]))
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
