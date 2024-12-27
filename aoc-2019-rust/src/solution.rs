pub trait DaySolution {
    fn solve_part_1(&self, input: &str) -> Result<i32, String>;
    fn solve_part_2(&self, input: &str) -> Result<i32, String>;
}
