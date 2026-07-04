-- ==========================================================
-- Script    : 00_Drop_Gold_Objects.sql
-- Purpose   : Drop all Gold Warehouse Tables
-- Project   : Fabric AI Customer Intelligence
-- ==========================================================

/*===========================================================
    FACT TABLES
===========================================================*/

DROP TABLE IF EXISTS Facts.FactCustomerSentiment;
GO

DROP TABLE IF EXISTS Facts.FactReviews;
GO

DROP TABLE IF EXISTS Facts.FactSales;
GO

/*===========================================================
    DIMENSION TABLES
===========================================================*/

DROP TABLE IF EXISTS Dimensions.DimPaymentMethod;
GO

DROP TABLE IF EXISTS Dimensions.DimDate;
GO

DROP TABLE IF EXISTS Dimensions.DimProduct;
GO

DROP TABLE IF EXISTS Dimensions.DimCustomer;
GO

PRINT 'All Gold tables dropped successfully.';
