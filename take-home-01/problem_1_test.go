package take_home_01

import (
	"testing"
)

func TestReverse(t *testing.T) {
	inputs := []int32{
		0,
		1,
		2,
		123,
		4321,
		// -1,
		2000000000,
		2000000009,
	}
	expectedAnswers := []int32{
		0,
		1,
		2,
		321,
		1234,
		// -1,
		2,
		0,
	}
	answers := make([]int32, 0)
	for _, input := range inputs {
		answers = append(answers, Reverse(input))
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

func TestCheckOverflowMultiply(t *testing.T) {
	inputs := [][]int32{
		{1, 2},
		// {-1, 2},
		// {-1, -1},
		// {-10, -10},
		{2000000000, 1},
		{2000000009, 2},
	}
	expectedAnswers := []bool{
		false,
		// false,
		// false,
		// false,
		false,
		true,
	}
	answers := make([]bool, 0)
	for _, input := range inputs {
		answers = append(answers, CheckOverflowMultiply(input[0], input[1]))
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

func TestCheckOverflowAdd(t *testing.T) {
	inputs := [][]int32{
		{1, 2},
		{2000000009, 2000000009},
	}
	expectedAnswers := []bool{
		false,
		true,
	}
	answers := make([]bool, 0)
	for _, input := range inputs {
		answers = append(answers, CheckOverflowAdd(input[0], input[1]))
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
