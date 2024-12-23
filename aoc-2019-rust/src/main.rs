mod day_1;
mod input;

use std::env;
// use std::fs;

#[derive(Debug)]
struct Day {
    /// The day number, e.g. 1, 2, 3, etc.
    number: u8,
    /// The part number. Should be 1 or 2.
    ///
    /// TODO: make sure that part is either 1 or 2.
    part: u8,
}

impl PartialEq for Day {
    fn eq(&self, other: &Self) -> bool {
        self.number == other.number && self.part == other.part
    }
}

fn parse_arg(arg: &str) -> Result<Day, String> {
    let (number_str, part_str) = arg.split_once('-').ok_or_else(|| {
        format!(
            "Argument should be in the format 'day-part' (1-1 or 2-2): {}",
            arg
        )
    })?;

    let number = number_str
        .parse::<u8>()
        .map_err(|_| format!("Day number should be between 1 and 25: {}", number_str))?;
    if number < 1 || number > 25 {
        return Err(format!(
            "Day number should be between 1 and 25: {}",
            number_str
        ));
    }

    let part = part_str
        .parse::<u8>()
        .map_err(|_| format!("Part number should be either 1 or 2: {}", part_str))?;
    if part < 1 || part > 2 {
        return Err(format!("Part number should be either 1 or 2: {}", part_str));
    }

    Ok(Day { number, part })
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn success() {
        assert_eq!(parse_arg("1-1").unwrap(), Day { number: 1, part: 1 },);
        assert_eq!(parse_arg("1-2").unwrap(), Day { number: 1, part: 2 });
        assert_eq!(parse_arg("2-1").unwrap(), Day { number: 2, part: 1 });
        assert_eq!(parse_arg("2-2").unwrap(), Day { number: 2, part: 2 });
    }

    #[test]
    fn invalid_day_number() {
        assert!(parse_arg("0-1").is_err());
        assert!(parse_arg("26-1").is_err());
        assert!(parse_arg("a-1").is_err());
        assert!(parse_arg("b-1").is_err());
    }

    #[test]
    fn invalid_day_part() {
        assert!(parse_arg("1-0").is_err());
        assert!(parse_arg("1-a").is_err());
        assert!(parse_arg("1-b").is_err());
        assert!(parse_arg("1-3").is_err());
    }
}

fn print_version() {
    println!("v0.1.0");
}

fn print_help() {
    println!("aoc-2019, a Rust program for Advent of Code 2019!");
    println!();
    println!("Usage:");
    println!();
    println!("  aoc-2019 [day-number]-[part-number]   run the code for the given day and part");
    println!("  aoc-2019 --help                       print this help message");
    println!("  aoc-2019 --version                    print the version number");
}

fn main() {
    let args: Vec<String> = env::args().collect();
    match args.len() {
        2 => match args[1].as_str() {
            "--help" => print_help(),
            "--version" => print_version(),
            arg => match parse_arg(arg) {
                Ok(Day { number: day_number, part }) => {
                    println!("Running solution for day {} part {}", day_number, part);
                    let _input = input::read(day_number).unwrap();
                    match (day_number, part) {
                        (1, 1) => {
                            let part_1_result = day_1::solve_part_1(&_input);
                            println!("Part 1 result: {part_1_result:?}");
                        }
                        (1, 2) => {
                            let part_2_result = day_1::solve_part_2(&_input);
                            println!("Part 2 result: {part_2_result:?}");
                        }
                        (2, 1) => {}
                        _ => panic!("Unimplemented code for day {} part {}", day_number, part),
                    };
                }
                Err(error) => println!("Error: {}", error),
            },
        },
        _ => print_help(),
    }
}
