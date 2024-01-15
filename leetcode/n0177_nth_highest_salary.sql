CREATE OR REPLACE FUNCTION NthHighestSalary(N INT) RETURNS TABLE (Salary INT) AS $$
BEGIN
  RETURN QUERY (
    WITH salaries_ranked AS (
        SELECT
            DENSE_RANK() OVER (ORDER BY e.salary DESC) AS ranking,
            e.salary
        FROM Employee e
    )
    SELECT max(salaries_ranked.salary)
    FROM salaries_ranked
    WHERE salaries_ranked.ranking = N
  );
END;
$$ LANGUAGE plpgsql;