CREATE OR ALTER VIEW Reporting.vwProductPerformance
AS

WITH SalesAgg AS
(
    SELECT

        ProductID,

        COUNT(OrderID) AS TotalOrders,

        SUM(Quantity) AS UnitsSold,

        SUM(TotalAmount) AS Revenue

    FROM Facts.FactSales

    GROUP BY ProductID
),

ReviewAgg AS
(
    SELECT

        ProductID,

        COUNT(*) AS ReviewCount,

        AVG(Rating) AS AverageRating

    FROM Facts.FactReviews

    GROUP BY ProductID
),

SentimentAgg AS
(
    SELECT

        ProductID,

        SUM(CASE WHEN Sentiment='Positive' THEN 1 ELSE 0 END) AS PositiveReviews,

        SUM(CASE WHEN Sentiment='Neutral' THEN 1 ELSE 0 END) AS NeutralReviews,

        SUM(CASE WHEN Sentiment='Negative' THEN 1 ELSE 0 END) AS NegativeReviews

    FROM Facts.FactCustomerSentiment

    GROUP BY ProductID
)

SELECT

    p.ProductID,

    p.ProductName,

    p.Category,

    ISNULL(s.TotalOrders,0) AS TotalOrders,

    ISNULL(s.UnitsSold,0) AS UnitsSold,

    ISNULL(s.Revenue,0) AS Revenue,

    ISNULL(r.ReviewCount,0) AS ReviewCount,

    ISNULL(r.AverageRating,0) AS AverageRating,

    ISNULL(se.PositiveReviews,0) AS PositiveReviews,

    ISNULL(se.NeutralReviews,0) AS NeutralReviews,

    ISNULL(se.NegativeReviews,0) AS NegativeReviews

FROM Dimensions.DimProduct p

LEFT JOIN SalesAgg s
ON p.ProductID=s.ProductID

LEFT JOIN ReviewAgg r
ON p.ProductID=r.ProductID

LEFT JOIN SentimentAgg se
ON p.ProductID=se.ProductID;
GO
