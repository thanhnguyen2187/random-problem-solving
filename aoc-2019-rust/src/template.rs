use crate::solution::DaySolution;

pub fn parse_input(input: &str) -> Result<Vec<i32>, String> {
    unimplemented!()
}

#[cfg(test)]
mod tests {
    use super::*;

    mod parse_input {
        use super::*;
        #[test]
        fn success() {
            assert_eq!(true);
        }
    }
}

pub fn solve_part_1(input: &str) -> Result<i32, String> {
    unimplemented!()
}

pub fn solve_part_2(input: &str) -> Result<i32, String> {
    unimplemented!()
}

pub struct DayN {}

impl DaySolution for DayN {
    fn solve_part_1(&self, input: &str) -> Result<i32, String> {
        solve_part_1(input)
    }

    fn solve_part_2(&self, input: &str) -> Result<i32, String> {
        solve_part_2(input)
    }
}
