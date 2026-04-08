CREATE OR REPLACE FUNCTION get_contacts_by_pattern(p text)
RETURNS TABLE(name VARCHAR, phone VARCHAR) AS $$
BEGIN
    RETURN QUERY 
    SELECT c.name, c.phone 
    FROM phonebook c
    WHERE c.name ILIKE '%' || p || '%'
       OR c.phone ILIKE '%' || p || '%';
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION get_contacts_paginated(p_limit INT, p_offset INT)
RETURNS TABLE(id INT, name VARCHAR, phone VARCHAR) AS $$
BEGIN
    RETURN QUERY
    SELECT c.id, c.name, c.phone
    FROM phonebook c
    LIMIT p_limit OFFSET p_offset;
END;
$$ LANGUAGE plpgsql;



-- -- поиск
-- CREATE OR REPLACE FUNCTION get_contacts_by_pattern(p text)
-- RETURNS TABLE(name VARCHAR, phone VARCHAR) AS $$
-- BEGIN
--     RETURN QUERY 
--     SELECT name, phone FROM phonebook
--     WHERE name ILIKE '%' || p || '%'
--        OR phone ILIKE '%' || p || '%';
-- END;
-- $$ LANGUAGE plpgsql;

-- -- пагинация
-- CREATE OR REPLACE FUNCTION get_contacts_paginated(p_limit INT, p_offset INT)
-- RETURNS TABLE(id INT, name VARCHAR, phone VARCHAR) AS $$
-- BEGIN
--     RETURN QUERY
--     SELECT * FROM phonebook
--     LIMIT p_limit OFFSET p_offset;
-- END;
-- $$ LANGUAGE plpgsql;