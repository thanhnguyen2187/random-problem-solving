pub fn read(day: u8) -> Result<String, String> {
    let path = format!("inputs/input_{}.txt", day);
    let contents_result = std::fs::read_to_string(path);
    match contents_result {
        Ok(contents) => Ok(contents),
        Err(error) => Err(format!("Could not read input file: {}", error)),
    }
}