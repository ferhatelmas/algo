SELECT c.Name
FROM Customers AS c LEFT JOIN Orders AS o ON c.Id = o.CustomerId
WHERE o.customerId IS NULL;
