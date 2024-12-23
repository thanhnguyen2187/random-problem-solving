pub fn parse_input(input: &str) -> Result<Vec<i32>, String> {
    input
        .lines()
        .map(|line| {
            line.trim()
                .parse::<i32>()
                .map_err(|err| format!("Failed to parse '{line}' as number: {err}"))
        })
        .collect() // Collects into Result<Vec<i32>, String>
}

pub fn calculate_fuel_required(mass: i32) -> i32 {
    (mass / 3) - 2
}

pub fn calculate_fuel_required_2(mass: i32) -> i32 {
    let fuel = (mass / 3) - 2;
    if fuel <= 0 {
        0
    } else {
        fuel + calculate_fuel_required_2(fuel)
    }
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

        #[test]
        fn required_2() {
            let fuels = [14, 1969, 100756].map(calculate_fuel_required_2);
            assert_eq!(fuels, [2, 966, 50346]);
        }
    }
}

pub fn solve_part_1(input: &str) -> Result<i32, String> {
    // let result = parse_input(input).map(|masses| masses.map(calculate_fuel_required).sum::<i32>());
    // println!("{result:?}");
    let masses = parse_input(input)?;
    let total_fuel = masses.iter().map(|mass| calculate_fuel_required(*mass)).sum::<i32>();
    Ok(total_fuel)
}

pub fn solve_part_2(input: &str) -> Result<i32, String> {
    let masses = parse_input(input)?;
    let total_fuel = masses.iter().map(|mass| calculate_fuel_required_2(*mass)).sum::<i32>();
    Ok(total_fuel)
}
