SELECT d.Name as Department, e.Name as Employee, e.Salary
FROM Department as d join Employee as e on d.Id = e.DepartmentId
WHERE e.Salary = (
    SELECT max(e1.Salary)
    FROM Employee as e1
    WHERE e1.DepartmentId = d.Id
)
GROUP BY Department, Employee;
