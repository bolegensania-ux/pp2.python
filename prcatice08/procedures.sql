CREATE OR REPLACE PROCEDURE insert_or_update_user(p_name Text, p_number TEXT)
AS $$
BEGIN 
    IF EXISTS(
        SELECT 1 FROM Phonebook WHERE name = p_name
    ) THEN 
        UPDATE Phonebook 
        SET number = p_number
        WHERE name = p_name;
    ELSE
        INSERT INTO Phonebook(name, number) 
        VALUES (p_name, p_number);
    END IF;
END;
$$LANGUAGE plpgsql;

CALL insert_or_update_user('Sasha', '999999');