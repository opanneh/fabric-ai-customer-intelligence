-- ==========================================================
-- Script    : 03_CreateFacts.sql
-- Purpose   : Create Gold Fact Tables
-- ==========================================================

/*===========================================================
    FactSales
===========================================================*/

DROP TABLE IF EXISTS Facts.FactSales;
GO

CREATE TABLE Facts.FactSales
(
    OrderID VARCHAR(8000),

    CustomerID VARCHAR(8000),

    ProductID VARCHAR(8000),

    OrderDate DATETIME2(6),

    Quantity INT,

    TotalAmount FLOAT,

    PaymentMethod VARCHAR(200)
);
GO

/*===========================================================
    FactReviews
===========================================================*/

DROP TABLE IF EXISTS Facts.FactReviews;
GO

CREATE TABLE Facts.FactReviews
(
    CustomerID VARCHAR(8000),

    ProductID VARCHAR(8000),

    Rating BIGINT,

    ReviewText VARCHAR(8000),

    ReviewTimestamp BIGINT
);
GO

/*===========================================================
    FactCustomerSentiment
===========================================================*/

DROP TABLE IF EXISTS Facts.FactCustomerSentiment;
GO

CREATE TABLE Facts.FactCustomerSentiment
(
    CustomerID VARCHAR(8000),

    ProductID VARCHAR(8000),

    Rating BIGINT,

    ReviewText VARCHAR(8000),

    ReviewTimestamp BIGINT,

    Sentiment VARCHAR(100),

    Category VARCHAR(500),

    Priority VARCHAR(100),

    Summary VARCHAR(8000),

    Keywords VARCHAR(8000),

    RecommendedAction VARCHAR(8000),

    AIModel VARCHAR(200),

    AnalysisTimestamp DATETIME2(6)
);
GO

PRINT 'Fact tables created successfully.';
