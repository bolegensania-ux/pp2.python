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


CREATE OR REPLACE PROCEDURE delete_user(p_value TEXT)
AS $$
BEGIN
    IF EXISTS(
        SELECT 1 FROM Phonebook WHERE name = p_name OR number = p_value
    ) THEN 
        DELETE FROM Phonebook 
	    WHERE name = p_value OR number = p_value;
END;
$$ LANGUAGE plpgsql;

CALL delete_user('Sasha');


CREATE OR REPLACE PROCEDURE insert_many_users()
AS $$
DECLARE
    rec RECORD;
BEGIN
    CREATE TEMP TABLE IF NOT EXISTS invalid_data (
        name TEXT,
        number TEXT
    );

    DELETE FROM invalid_data;

    FOR rec IN SELECT * FROM phonebook_temp
    LOOP
        IF rec.number ~ '^[0-9]+$' THEN
            INSERT INTO phonebook(name, number)
            VALUES (rec.name, rec.number)
            ON CONFLICT (number) DO NOTHING;
        ELSE
            -- store invalid data
            INSERT INTO invalid_data(name, number)
            VALUES (rec.name, rec.number);
        END IF;
    END LOOP;
END;
$$ LANGUAGE plpgsql;