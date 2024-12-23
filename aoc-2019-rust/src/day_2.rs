pub fn parse_input(input: &str) -> Result<Vec<u32>, String> {
    input
        .split(',')
        .map(|line| {
            line.trim()
                .parse::<u32>()
                .map_err(|err| format!("Failed to parse '{line}' as number: {err}"))
        })
        .collect()
}

pub fn evaluate(opcodes: &mut Vec<u32>) -> Result<(), String> {
    let mut index: usize = 0;
    while index < opcodes.len() || opcodes[index] != 99 {
        let opcode = opcodes[index];
        match opcode {
            1 => {
                let a = opcodes[index + 1] as usize;
                let b = opcodes[index + 2] as usize;
                let c = opcodes[index + 3] as usize;
                let value = opcodes[a] + opcodes[b];
                opcodes[c] = value;
            }
            2 => {
                let a = opcodes[index + 1] as usize;
                let b = opcodes[index + 2] as usize;
                let c = opcodes[index + 3] as usize;
                let value = opcodes[a] * opcodes[b];
                opcodes[c] = value;
            }
            99 => break,
            _ => return Err(format!("Unknown opcode: {}", opcodes[index])),
        }
        index += 4;
    }

    Ok(())
}

#[cfg(test)]
mod tests {
    use super::*;

    mod parse_input {
        use super::*;
        #[test]
        fn success() {
            let input = r#"1,2,3,4"#;
            let numbers = parse_input(input).unwrap();
            assert_eq!(numbers, vec![1, 2, 3, 4]);
        }

        #[test]
        fn failure() {
            let input = r#"a,b,c"#;
            assert!(parse_input(input).is_err());
        }
    }

    mod evaluate {
        use super::*;

        #[test]
        fn success() {
            {
                let mut opcodes = vec![1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50];
                evaluate(&mut opcodes).unwrap();
                assert_eq!(opcodes, vec![3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50]);
            }
            {
                let mut opcodes = vec![1, 0, 0, 0, 99];
                evaluate(&mut opcodes).unwrap();
                assert_eq!(opcodes, vec![2, 0, 0, 0, 99]);
            }
            {
                let mut opcodes = vec![2, 3, 0, 3, 99];
                evaluate(&mut opcodes).unwrap();
                assert_eq!(opcodes, vec![2, 3, 0, 6, 99]);
            }
            {
                let mut opcodes = vec![2, 4, 4, 5, 99, 0];
                evaluate(&mut opcodes).unwrap();
                assert_eq!(opcodes, vec![2, 4, 4, 5, 99, 9801]);
            }
            {
                let mut opcodes = vec![1, 1, 1, 4, 99, 5, 6, 0, 99];
                evaluate(&mut opcodes).unwrap();
                assert_eq!(opcodes, vec![30, 1, 1, 4, 2, 5, 6, 0, 99]);
            }
        }

        #[test]
        fn required_2() {}
    }
}

pub fn solve_part_1(input: &str) -> Result<u32, String> {
    let mut opcodes = parse_input(input)?;
    evaluate(&mut opcodes)?;
    Ok(opcodes[0])
}

// pub fn solve_part_2(input: &str) -> Result<i32, String> {
//     let masses = parse_input(input)?;
//     let total_fuel = masses.iter().map(|mass| calculate_fuel_required_2(*mass)).sum::<i32>();
//     Ok(total_fuel)
// }
