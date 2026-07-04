-- ==========================================================
-- Script    : 07_vwCustomer360.sql
-- Purpose   : Create Customer 360 reporting view combining
--             customer, sales, reviews and AI sentiment
--             insights into a single analytical dataset.
-- Source    : DimCustomer, FactSales,
--             FactReviews, FactCustomerSentiment
-- Output    : Reporting.vwCustomer360
-- ==========================================================

CREATE OR ALTER VIEW Reporting.vwCustomer360
AS

WITH SalesAgg AS
(
    SELECT

        CustomerID,

        COUNT(OrderID) AS TotalOrders,

        SUM(TotalAmount) AS TotalRevenue,

        AVG(TotalAmount) AS AverageOrderValue

    FROM Facts.FactSales

    GROUP BY CustomerID
),

ReviewAgg AS
(
    SELECT

        CustomerID,

        COUNT(*) AS ReviewCount,

        AVG(Rating) AS AverageRating

    FROM Facts.FactReviews

    GROUP BY CustomerID
),

SentimentAgg AS
(
    SELECT

        CustomerID,

        SUM(CASE WHEN Sentiment='Positive' THEN 1 ELSE 0 END) AS PositiveReviews,

        SUM(CASE WHEN Sentiment='Neutral' THEN 1 ELSE 0 END) AS NeutralReviews,

        SUM(CASE WHEN Sentiment='Negative' THEN 1 ELSE 0 END) AS NegativeReviews

    FROM Facts.FactCustomerSentiment

    GROUP BY CustomerID
)

SELECT

    c.CustomerID,

    c.CustomerName,

    c.Email,

    c.Location,

    c.SignupDate,

    ISNULL(s.TotalOrders,0) AS TotalOrders,

    ISNULL(s.TotalRevenue,0) AS TotalRevenue,

    ISNULL(s.AverageOrderValue,0) AS AverageOrderValue,

    ISNULL(r.ReviewCount,0) AS ReviewCount,

    ISNULL(r.AverageRating,0) AS AverageRating,

    ISNULL(se.PositiveReviews,0) AS PositiveReviews,

    ISNULL(se.NeutralReviews,0) AS NeutralReviews,

    ISNULL(se.NegativeReviews,0) AS NegativeReviews

FROM Dimensions.DimCustomer c

LEFT JOIN SalesAgg s
ON c.CustomerID=s.CustomerID

LEFT JOIN ReviewAgg r
ON c.CustomerID=r.CustomerID

LEFT JOIN SentimentAgg se
ON c.CustomerID=se.CustomerID;
GO
