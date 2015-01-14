select
    distinct(a.Num)
from
    Logs as a,
    Logs as b,
    Logs as c
where
    a.Id=b.Id-1 and
    b.Id=c.Id-1 and
    a.Num=b.Num and
    b.Num=c.Num;
