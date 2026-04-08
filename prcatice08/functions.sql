CREATE OR REPLACE FUNCTION search_phonebook(pattern TEXT)
RETURNS TABLE(id INT, name TEXT, number TEXT)
AS $$
    SELECT id, name, number
    FROM Phonebook 
    WHERE name ILIKE '%' || pattern || '%'
       OR number ILIKE '%' || pattern || '%';
$$ LANGUAGE sql;

SELECT * FROM search_phonebook('Sa');