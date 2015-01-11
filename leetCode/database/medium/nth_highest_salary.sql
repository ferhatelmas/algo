CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      select E.Salary
      from (
        select @row := @row + 1 as row, e.Salary
        from (
            select distinct(Salary)
            from Employee
            order by Salary desc
        ) as e, (SELECT @row := 0) r
      ) as E
      where E.row = N
  );
END
