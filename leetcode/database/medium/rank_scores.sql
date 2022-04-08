select
    Score,
    (
        select
            count(distinct(Score))+1
        from
            Scores
        where
            Score > s.Score
    ) as Rank
from
    Scores as s
order by
    Score desc;
