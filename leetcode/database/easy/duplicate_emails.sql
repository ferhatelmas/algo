SELECT DISTINCT p1.Email
FROM Person AS p1
HAVING (
    SELECT count(p2.Id)
    FROM Person AS p2
    WHERE p2.Email = p1.Email
) > 1;
