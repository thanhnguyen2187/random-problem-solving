WITH EmployeeExtended AS (
    SELECT e.name, e.salary, m.salary AS managerSalary
    FROM Employee e
    JOIN Employee m
    ON e.managerId = m.id
)
SELECT name AS Employee
FROM EmployeeExtended
WHERE salary > managerSalary;