CREATE OR ALTER VIEW Reporting.vwExecutiveSales
AS

SELECT

    CAST(OrderDate AS DATE) AS OrderDate,

    COUNT(OrderID) AS TotalOrders,

    COUNT(DISTINCT CustomerID) AS TotalCustomers,

    COUNT(DISTINCT ProductID) AS TotalProducts,

    SUM(Quantity) AS UnitsSold,

    SUM(TotalAmount) AS Revenue,

    AVG(TotalAmount) AS AverageOrderValue

FROM Facts.FactSales

GROUP BY CAST(OrderDate AS DATE);
GO
