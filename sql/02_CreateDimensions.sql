-- ==========================================================
-- Script    : 02_CreateDimensions.sql
-- Purpose   : Create Gold Dimension Tables
-- ==========================================================

/*===========================================================
    DimCustomer
===========================================================*/

DROP TABLE IF EXISTS Dimensions.DimCustomer;
GO

CREATE TABLE Dimensions.DimCustomer
(
    CustomerID VARCHAR(8000),

    CustomerName VARCHAR(8000),

    Email VARCHAR(8000),

    Location VARCHAR(8000),

    SignupDate DATE
);
GO

/*===========================================================
    DimProduct
===========================================================*/

DROP TABLE IF EXISTS Dimensions.DimProduct;
GO

CREATE TABLE Dimensions.DimProduct
(
    ProductID VARCHAR(8000),

    ProductName VARCHAR(8000),

    Category VARCHAR(8000)
);
GO

/*===========================================================
    DimDate
===========================================================*/

DROP TABLE IF EXISTS Dimensions.DimDate;
GO

CREATE TABLE Dimensions.DimDate
(
    CalendarDate DATE,

    DayNumber INT,

    MonthNumber INT,

    MonthName VARCHAR(20),

    QuarterNumber INT,

    YearNumber INT
);
GO

PRINT 'Dimension tables created successfully.';
