SELECT
    d.Name AS Department, r.Name AS Employee, r.Salary
FROM
    Department AS d JOIN (
        SELECT
            e.Id, e.Name, e.Salary, e.DepartmentId, (
                SELECT
                    COUNT(DISTINCT e1.Salary)
                FROM
                    Employee AS e1
                WHERE
                    e1.Salary >= e.Salary AND e1.DepartmentId = e.DepartmentId AND e1.Id <> e.Id
            ) AS Rank
        FROM Employee as e
    ) AS r ON r.DepartmentId = d.Id
WHERE r.Rank < 3
ORDER BY d.Name, r.Salary DESC;
