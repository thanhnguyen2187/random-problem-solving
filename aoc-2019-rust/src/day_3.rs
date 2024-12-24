use std::cmp::{min};
use std::collections::HashMap;
use std::collections::HashSet;

/// Denotes how a wire moves.
#[derive(Debug, PartialEq)]
pub enum Step {
    Up(i16),
    Down(i16),
    Left(i16),
    Right(i16),
}

#[derive(Debug, PartialEq, Eq, Hash, Copy, Clone)]
pub struct Position {
    x: i16,
    y: i16,
}

type PairPositionDistance = (Position, i16);

pub fn parse_input(input: &str) -> Result<Vec<Vec<Step>>, String> {
    input
        .lines()
        .map(parse_line)
        .collect()
}

pub fn parse_line(line: &str) -> Result<Vec<Step>, String> {
    line
        .split(',')
        .map(|word| {
            let word = word.trim();
            match word.chars().next() {
                Some('U') => {
                    let distance = word[1..].parse::<i16>().map_err(|err| {
                        format!("Failed to parse '{word}' to step: {err}")
                    })?;
                    Ok(Step::Up(distance))
                }
                Some('D') => {
                    let distance = word[1..].parse::<i16>().map_err(|err| {
                        format!("Failed to parse '{word}' to step: {err}")
                    })?;
                    Ok(Step::Down(distance))
                }
                Some('L') => {
                    let distance = word[1..].parse::<i16>().map_err(|err| {
                        format!("Failed to parse '{word}' to step: {err}")
                    })?;
                    Ok(Step::Left(distance))
                }
                Some('R') => {
                    let distance = word[1..].parse::<i16>().map_err(|err| {
                        format!("Failed to parse '{word}' to step: {err}")
                    })?;
                    Ok(Step::Right(distance))
                }
                _ => Err(format!("Failed to parse '{word}' to step")),
            }
        })
        .collect()
}

pub fn calculate_position_last(
    position_current: Position,
    step: &Step,
) -> Position {
    match step {
        Step::Up(distance) => {
            Position {
                x: position_current.x,
                y: position_current.y + distance,
            }
        }
        Step::Down(distance) => {
            Position {
                x: position_current.x,
                y: position_current.y - distance,
            }
        }
        Step::Left(distance) => {
            Position {
                x: position_current.x - distance,
                y: position_current.y,
            }
        }
        Step::Right(distance) => {
            Position {
                x: position_current.x + distance,
                y: position_current.y,
            }
        }
    }
}

/// Calculates the positions that the wire will take after a particular step. Also returns the
/// wire's position after the step.
pub fn calculate_wire_positions(
    position_current: Position,
    step: &Step,
) -> (HashSet<Position>, Position) {
    let position_last = calculate_position_last(position_current, step);
    let mut positions = HashSet::new();
    let mut position_running = position_current;
    loop {
        match step {
            Step::Up(_) => {
                position_running.y += 1;
            }
            Step::Down(_) => {
                position_running.y -= 1;
            }
            Step::Left(_) => {
                position_running.x -= 1;
            }
            Step::Right(_) => {
                position_running.x += 1;
            }
        }
        positions.insert(position_running.clone());
        if position_running == position_last {
            break;
        }
    }

    (positions, position_last)
}

pub fn calculate_wire_positions_all(
    position_start: Position,
    steps: &Vec<Step>,
) -> HashSet<Position> {
    let mut positions = HashSet::new();
    let mut position_running = position_start;
    for step in steps {
        let (positions_step, position_last_step) =
            calculate_wire_positions(position_running, step);
        positions.extend(positions_step);
        position_running = position_last_step;
    }
    positions
}

/// Calculates for each position, which wires is going to pass through it.
pub fn calculate_positions_recorder(
    position_start: Position,
    wires_steps: Vec<Vec<Step>>,
) -> HashMap<Position, HashSet<usize>> {
    let mut recorder = HashMap::new();

    for (wire_index, wire_steps) in wires_steps.iter().enumerate() {
        let positions =
            calculate_wire_positions_all(position_start, wire_steps);
        for position in positions {
            recorder
                .entry(position)
                .or_insert(HashSet::new())
                .insert(wire_index);
        }
    }

    recorder
}

// Calculates the positions that the wires will pass through and corresponding distances.
pub fn calculate_pairs_position_distance(
    position_start: Position,
    distance_start: i16,
    step: &Step,
) -> Vec<PairPositionDistance> {
    let mut position_running = position_start;
    let mut pairs: Vec<PairPositionDistance> = Vec::new();
    let mut distance = distance_start;
    let position_last = calculate_position_last(position_running, step);
    while position_running != position_last {
        match step {
            Step::Up(_) => {
                position_running.y += 1;
            }
            Step::Down(_) => {
                position_running.y -= 1;
            }
            Step::Left(_) => {
                position_running.x -= 1;
            }
            Step::Right(_) => {
                position_running.x += 1;
            }
        }
        distance += 1;
        pairs.push((position_running.clone(), distance));
    }

    pairs
}

pub fn calculate_pairs_position_distance_all(
    position_start: Position,
    steps: &Vec<Step>,
) -> Vec<(Position, i16)> {
    let mut pairs_all = Vec::new();
    let mut distance_running = 0;
    let mut position_running = position_start;
    for step in steps {
        let pairs =
            calculate_pairs_position_distance(
                position_running,
                distance_running,
                step,
            );
        position_running = pairs.last().unwrap().0;
        distance_running = pairs.last().unwrap().1;
        pairs_all.extend(pairs);
    }
    pairs_all
}

pub fn calculate_manhattan_distance(position1: Position, position2: Position) -> i16 {
    (position1.x - position2.x).abs() +
        (position1.y - position2.y).abs()
}

#[cfg(test)]
mod tests {
    use super::*;

    mod parse_line {
        use super::*;
        #[test]
        fn success() {
            let line = r#"R8,U5,L5,D3"#;
            let steps = parse_line(line).unwrap();
            assert_eq!(steps, vec![Step::Right(8), Step::Up(5), Step::Left(5), Step::Down(3)]);
        }

        #[test]
        fn success_prefix_space() {
            let line = r#"   R8,U5,L5,D3"#;
            let steps = parse_line(line).unwrap();
            assert_eq!(steps, vec![Step::Right(8), Step::Up(5), Step::Left(5), Step::Down(3)]);
        }

        #[test]
        fn success_suffix_space() {
            let line = r#"R8,U5,L5,D3  "#;
            let steps = parse_line(line).unwrap();
            assert_eq!(steps, vec![Step::Right(8), Step::Up(5), Step::Left(5), Step::Down(3)]);
        }

        #[test]
        fn failure() {
            let line = r#"a1"#;
            assert!(parse_line(line).is_err());
        }
    }

    mod parse_input {
        use super::*;
        #[test]
        fn success() {
            let input = r#"R8,U5,L5,D3
            R4,D4
            R4,U4,L8
            U7,R3,D1
            L3,U0,R0
            D1,R2,U5"#;
            let steps = parse_input(input).unwrap();
            assert_eq!(steps, vec![
                vec![Step::Right(8), Step::Up(5), Step::Left(5), Step::Down(3)],
                vec![Step::Right(4), Step::Down(4)],
                vec![Step::Right(4), Step::Up(4), Step::Left(8)],
                vec![Step::Up(7), Step::Right(3), Step::Down(1)],
                vec![Step::Left(3), Step::Up(0), Step::Right(0)],
                vec![Step::Down(1), Step::Right(2), Step::Up(5)],
            ]);
        }
    }

    mod calculate_wire_positions {
        use super::*;

        #[test]
        fn success() {
            let position_current = Position { x: 0, y: 0 };
            {
                let step = Step::Right(2);
                let (positions, position_last) =
                    calculate_wire_positions(position_current, &step);
                assert_eq!(positions, HashSet::from_iter(vec![
                    Position { x: 1, y: 0 },
                    Position { x: 2, y: 0 },
                ].iter().cloned()));
            }
            {
                let step = Step::Up(2);
                let (positions, position_last) =
                    calculate_wire_positions(position_current, &step);
                assert_eq!(positions, HashSet::from_iter(vec![
                    Position { x: 0, y: 1 },
                    Position { x: 0, y: 2 },
                ].iter().cloned()));
            }
        }
    }

    mod calculate_wire_positions_all {
        use super::*;

        #[test]
        fn success() {
            let position_start = Position { x: 0, y: 0 };
            let steps = vec![
                Step::Right(2),
                Step::Up(2),
                Step::Left(2),
                Step::Down(2),
            ];
            let positions = calculate_wire_positions_all(position_start, &steps);
            assert_eq!(positions, HashSet::from_iter(vec![
                // Position { x: 0, y: 0 },
                Position { x: 1, y: 0 },
                Position { x: 2, y: 0 },
                Position { x: 2, y: 1 },
                Position { x: 2, y: 2 },
                Position { x: 1, y: 2 },
                Position { x: 0, y: 2 },
                Position { x: 0, y: 1 },
                Position { x: 0, y: 0 },
            ].iter().cloned()));
        }
    }

    mod calculate_positions_recorder {
        use super::*;

        #[test]
        fn success() {
            // Reusing the example from the problem description:
            //
            // ```
            // ...........
            // .+-----+...
            // .|.....|...
            // .|..+--X-+.
            // .|..|..|.|.
            // .|.-X--+.|.
            // .|..|....|.
            // .|.......|.
            // .o-------+.
            // ...........
            // ```
            let position_start = Position { x: 0, y: 0 };
            let wires_steps = vec![
                vec![Step::Right(8), Step::Up(5), Step::Left(5), Step::Down(3)],
                vec![Step::Up(7), Step::Right(6), Step::Down(4), Step::Left(4)],
            ];
            let recorder = calculate_positions_recorder(position_start, wires_steps);
            let test_table = vec![
                // (Position { x: 0, y: 0 }, None),
                (Position { x: 8, y: 0 }, HashSet::from_iter(vec![0])),
                (Position { x: 0, y: 7 }, HashSet::from_iter(vec![1])),
                (Position { x: 3, y: 3 }, HashSet::from_iter(vec![0, 1])),
                (Position { x: 6, y: 5 }, HashSet::from_iter(vec![0, 1])),
            ];
            for (position, wires_expected) in test_table {
                let wires_got = recorder.get(&position).unwrap();
                assert_eq!(wires_got, &wires_expected);
            }
        }
    }

    mod calculate_pairs_position_distance {
        use super::*;

        #[test]
        fn success() {
            let position_start = Position { x: 0, y: 0 };
            let step = Step::Right(5);
            let pairs_position_distance =
                calculate_pairs_position_distance(
                    position_start,
                    0,
                    &step,
                );
            assert_eq!(pairs_position_distance, vec![
                (Position { x: 1, y: 0 }, 1),
                (Position { x: 2, y: 0 }, 2),
                (Position { x: 3, y: 0 }, 3),
                (Position { x: 4, y: 0 }, 4),
                (Position { x: 5, y: 0 }, 5),
            ]);
        }
    }

    mod calculate_pairs_position_distance_all {
        use super::*;

        #[test]
        fn success() {
            let position_start = Position { x: 0, y: 0 };
            let steps = vec![
                Step::Right(2),
                Step::Up(2),
                Step::Left(2),
                Step::Down(2),
            ];
            let pairs_position_distance_all =
                calculate_pairs_position_distance_all(
                    position_start,
                    &steps,
                );
            assert_eq!(pairs_position_distance_all, vec![
                (Position { x: 1, y: 0 }, 1),
                (Position { x: 2, y: 0 }, 2),
                (Position { x: 2, y: 1 }, 3),
                (Position { x: 2, y: 2 }, 4),
                (Position { x: 1, y: 2 }, 5),
                (Position { x: 0, y: 2 }, 6),
                (Position { x: 0, y: 1 }, 7),
                (Position { x: 0, y: 0 }, 8),
            ]);
        }
    }

    mod solve_part_1 {
        use super::*;

        #[test]
        fn success() {
            let input = r#"R8,U5,L5,D3
            U7,R6,D4,L4"#;
            let result = solve_part_1(input).unwrap();
            assert_eq!(result, 6);
        }

        #[test]
        fn success_2() {
            let input = r#"R75,D30,R83,U83,L12,D49,R71,U7,L72
            U62,R66,U55,R34,D71,R55,D58,R83"#;
            let result = solve_part_1(input).unwrap();
            assert_eq!(result, 159);
        }

        #[test]
        fn success_3() {
            let input = r#"R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51
            U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"#;
            let result = solve_part_1(input).unwrap();
            assert_eq!(result, 135);
        }
    }
}

pub fn solve_part_1(input: &str) -> Result<i16, String> {
    let wires_steps = parse_input(input)?;
    let position_start = Position { x: 0, y: 0 };
    let recorder =
        calculate_positions_recorder(
            position_start,
            wires_steps,
        );

    let mut distance_min = i16::MAX;
    for (position, wires) in recorder {
        if wires.len() == 1 || position == position_start {
            continue;
        }
        let distance = calculate_manhattan_distance(position, position_start);
        distance_min = min(distance_min, distance);
    }

    Ok(distance_min)
}

pub fn solve_part_2(input: &str) -> Result<u32, String> {
    let wires_steps = parse_input(input)?;
    let position_start = Position { x: 0, y: 0 };
    let recorder =
        calculate_positions_recorder(
            position_start,
            wires_steps,
        );

    let mut distance_min = i16::MAX;
    for (position, wires) in recorder {
        if wires.len() == 1 || position == position_start {
            continue;
        }
        let distance = calculate_manhattan_distance(position, position_start);
        distance_min = min(distance_min, distance);
    }
    Err("No solution found".to_string())
}
