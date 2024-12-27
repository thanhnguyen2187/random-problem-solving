use crate::solution::DaySolution;

pub fn parse_input(input: &str) -> Result<[i32; 2], String> {
    let (part_1, part_2) = input
        .split_once('-')
        .ok_or_else(|| "Input should be in the format '[part-1]-[part-2]'")?;

    Ok([
        part_1.parse::<i32>().map_err(|e| e.to_string())?,
        part_2.parse::<i32>().map_err(|e| e.to_string())?,
    ])
}

pub fn is_valid(password: i32) -> bool {
    let digits =
        password
            .to_string()
            .chars()
            .collect::<Vec<char>>();

    let pairs = digits
        .iter()
        .zip(digits.iter().skip(1));

    let mut duplicated = false;
    for (a, b) in pairs {
        if a > b {
            return false;
        }
        if a == b && !duplicated {
            duplicated = true;
        }
    }

    duplicated
}

#[cfg(test)]
mod tests {
    use super::*;

    mod parse_input {
        use super::*;

        #[test]
        fn success() {
            assert_eq!(parse_input("1-2").unwrap(), [1, 2]);
            assert_eq!(parse_input("3-4").unwrap(), [3, 4]);
        }

        #[test]
        fn failure() {
            assert!(parse_input("a-b").is_err());
            assert!(parse_input("").is_err());
        }
    }

    mod is_valid {
        use super::*;

        #[test]
        fn success() {
            let test_table = vec![
                (111111, true),
                (223450, false),
                (123789, false),
            ];

            for (password, expected) in test_table {
                assert_eq!(is_valid(password), expected);
            }
        }
    }
}

pub fn solve_part_1(input: &str) -> Result<i32, String> {
    let range = parse_input(input)?;

    let mut count = 0;
    for password in range[0]..=range[1] {
        if is_valid(password) {
            count += 1;
        }
    }

    Ok(count)
}

pub fn solve_part_2(input: &str) -> Result<i32, String> {
    unimplemented!()
}

pub struct Day4 {}

impl DaySolution for Day4 {
    fn solve_part_1(&self, input: &str) -> Result<i32, String> {
        solve_part_1(input)
    }

    fn solve_part_2(&self, input: &str) -> Result<i32, String> {
        solve_part_2(input)
    }
}
