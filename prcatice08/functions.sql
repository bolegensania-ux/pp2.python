CREATE OR REPLACE FUNCTION search_phonebook(pattern TEXT)
RETURNS TABLE(id INT, name TEXT, number TEXT)
AS $$
    SELECT id, name, number
    FROM Phonebook 
    WHERE name ILIKE '%' || pattern || '%'        LIKE '%Sa%'
       OR number ILIKE '%' || pattern || '%';
$$ LANGUAGE sql;

SELECT * FROM search_phonebook('Sa');


CREATE OR REPLACE FUNCTION get_phonebook_paginated(limit_val INT, offset_val INT)
RETURNS TABLE(id INT, name TEXT, number TEXT)
AS $$
    SELECT id, name, number
	FROM Phonebook
	ORDER BY id 
	LIMIT limit_val OFFSET offset_val;
$$ LANGUAGE sql;

SELECT * FROM get_phonebook_paginated(5, 0);



