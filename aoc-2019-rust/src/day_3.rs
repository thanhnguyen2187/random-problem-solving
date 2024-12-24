use std::collections::HashMap;
use std::collections::HashSet;

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

pub fn parse_input(input: &str) -> Result<Vec<Step>, String> {
    input
        .split(',')
        .map(|word| {
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

pub fn populate(
    wires: &mut HashMap<Position, i16>,
    position_current: Position,
    step: Step,
) -> Position {
    let position_last = match step {
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
    };
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
        let count_current = wires.get(&position_running).unwrap_or(&0);
        wires.insert(position_running.clone(), *count_current + 1);
        if position_running == position_last {
            break;
        }
    }

    position_last
}

#[cfg(test)]
mod tests {
    use super::*;

    mod parse_input {
        use super::*;
        #[test]
        fn success() {
            let input = r#"R8,U5,L5,D3"#;
            let steps = parse_input(input).unwrap();
            assert_eq!(steps, vec![Step::Right(8), Step::Up(5), Step::Left(5), Step::Down(3)]);
        }

        #[test]
        fn failure() {
            let input = r#"a1"#;
            assert!(parse_input(input).is_err());
        }
    }

    mod populate {
        use super::*;

        #[test]
        fn success() {
            let steps = vec![
                Step::Right(2),
                Step::Up(2),
                Step::Left(2),
                Step::Down(2),
            ];
            let mut positions = vec![
                Position { x: 0, y: 0 },
            ];
            let mut wires = HashMap::new();
            for step in steps {
                let position_next = populate(
                    &mut wires,
                    positions.last().unwrap().clone(),
                    step,
                );
                positions.push(position_next);
            }

            assert_eq!(positions, vec![
                Position { x: 0, y: 0 },
                Position { x: 2, y: 0 },
                Position { x: 2, y: 2 },
                Position { x: 0, y: 2 },
                Position { x: 0, y: 0 },
            ]);
            assert_eq!(wires, HashMap::from([
                (Position { x: 1, y: 0 }, 1),
                (Position { x: 2, y: 0 }, 1),
                (Position { x: 2, y: 1 }, 1),
                (Position { x: 2, y: 2 }, 1),
                (Position { x: 1, y: 2 }, 1),
                (Position { x: 0, y: 2 }, 1),
                (Position { x: 0, y: 1 }, 1),
                (Position { x: 0, y: 0 }, 1),
            ]));
        }

        #[test]
        fn required_2() {}
    }
}

// pub fn solve_part_1(input: &str) -> Result<u32, String> {
//     let mut opcodes = parse_input(input)?;
//     opcodes[1] = 12;
//     opcodes[2] = 2;
//     evaluate(&mut opcodes)?;
//     Ok(opcodes[0])
// }

// pub fn solve_part_2(input: &str) -> Result<u32, String> {
//     let opcodes_original = parse_input(input)?;
//     for (noun, verb) in (0..100).flat_map(|i| (0..100).map(move |j| (i, j))) {
//         let mut opcodes = opcodes_original.clone();
//         opcodes[1] = noun;
//         opcodes[2] = verb;
//         evaluate(&mut opcodes)?;
//         if opcodes[0] == 19690720 {
//             return Ok(noun * 100 + verb);
//         }
//     }
//     Err("No solution found".to_string())
// }
