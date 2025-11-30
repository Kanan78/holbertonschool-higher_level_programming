-- It ptints description of the table first_table from the database hbtn_0c_0
SELECT
    TABLE_NAME AS 'Table',
    COLUMN_NAME AS 'Field',
    COLUMN_TYPE AS 'Type',
    IS_NULLABLE AS 'Null',
    COLUMN_KEY AS 'Key',
    COLUMN_DEFAULT AS 'Default',
    EXTRA AS 'Extra'
FROM information_schema.COLUMNS
WHERE TABLE_SCHEMA = 'hbtn_0c_0'
  AND TABLE_NAME = 'first_table';

