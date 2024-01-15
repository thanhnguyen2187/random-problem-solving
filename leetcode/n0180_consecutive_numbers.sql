WITH nums_counter AS (
    SELECT
        num,
        LAG(num, 1) OVER(ORDER BY id) AS num_lag_1,
        LAG(num, 2) OVER(ORDER BY id) AS num_lag_2
    FROM logs
)
SELECT DISTINCT num AS ConsecutiveNums
FROM nums_counter
WHERE num = num_lag_1 and num = num_lag_2;