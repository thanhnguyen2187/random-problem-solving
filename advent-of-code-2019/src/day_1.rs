pub fn parse_input(input: &str) -> Result<Vec<u32>, String> {
    input
        .lines()
        .map(|line| {
            line.trim()
                .parse::<u32>()
                .map_err(|err| format!("Failed to parse '{line}' as number: {err}"))
        })
        .collect() // Collects into Result<Vec<i32>, String>
}

pub fn calculate_fuel_required(mass: &u32) -> u32 {
    (mass / 3) - 2
}

#[cfg(test)]
mod tests {
    use super::*;

    mod parse_input {
        use super::*;
        #[test]
        fn success() {
            let input = r#"1
        2
        3
        4"#;
            let numbers = parse_input(input).unwrap();
            assert_eq!(numbers, vec![1, 2, 3, 4]);
        }

        #[test]
        fn failure() {
            let input = r#"a
        b
        c"#;
            assert!(parse_input(input).is_err());
        }
    }

    mod calculate_fuel {
        use super::*;

        #[test]
        fn required() {
            let fuels = [12, 14, 1969, 100756].map(calculate_fuel_required);
            assert_eq!(fuels, [2, 2, 654, 33583]);
        }
    }
}

pub fn solve_part1(input: &str) -> Result<u32, String> {
    // let result = parse_input(input).map(|masses| masses.map(calculate_fuel_required).sum::<u32>());
    // println!("{result:?}");
    let masses = parse_input(input)?;
    let total_fuel = masses.iter().map(calculate_fuel_required).sum::<u32>();
    Ok(total_fuel)
}
