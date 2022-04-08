SELECT e1.Name
FROM Employee as e1 JOIN Employee as e2 ON e1.ManagerId = e2.id
WHERE e1.Salary > e2.Salary;
