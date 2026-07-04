-- ==========================================================
-- Script    : 01_CreateSchemas.sql
-- Purpose   : Create Warehouse Schemas
-- ==========================================================

-- Create Dimensions Schema

IF NOT EXISTS (
    SELECT *
    FROM sys.schemas
    WHERE name = 'Dimensions'
)
BEGIN
    EXEC ('CREATE SCHEMA Dimensions');
END;
GO

-- Create Facts Schema

IF NOT EXISTS (
    SELECT *
    FROM sys.schemas
    WHERE name = 'Facts'
)
BEGIN
    EXEC ('CREATE SCHEMA Facts');
END;
GO

-- Create Reporting Schema

IF NOT EXISTS (
    SELECT *
    FROM sys.schemas
    WHERE name = 'Reporting'
)
BEGIN
    EXEC ('CREATE SCHEMA Reporting');
END;
GO

PRINT 'Schemas created successfully.';
