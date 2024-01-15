WITH salaries_ranked AS (
    SELECT
        salary,
        DENSE_RANK() OVER (ORDER BY salary DESC) AS ranking
    FROM Employee
)
SELECT max(salary) AS SecondHighestSalary
FROM salaries_ranked
WHERE ranking = 2;