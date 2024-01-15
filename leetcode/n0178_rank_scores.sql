WITH ranked_scores AS (
    SELECT
        score,
        DENSE_RANK() OVER (ORDER BY score DESC) AS rank
    FROM scores
)
SELECT * FROM ranked_scores
ORDER BY rank;