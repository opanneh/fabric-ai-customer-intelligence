CREATE OR ALTER PROCEDURE Reporting.usp_DataQualitySummary
AS
BEGIN

    SET NOCOUNT ON;

    SELECT
        'DimCustomer' AS TableName,
        COUNT(*) AS TotalRows
    FROM Dimensions.DimCustomer

    UNION ALL

    SELECT
        'DimProduct',
        COUNT(*)
    FROM Dimensions.DimProduct

    UNION ALL

    SELECT
        'DimDate',
        COUNT(*)
    FROM Dimensions.DimDate

    UNION ALL

    SELECT
        'FactSales',
        COUNT(*)
    FROM Facts.FactSales

    UNION ALL

    SELECT
        'FactReviews',
        COUNT(*)
    FROM Facts.FactReviews

    UNION ALL

    SELECT
        'FactCustomerSentiment',
        COUNT(*)
    FROM Facts.FactCustomerSentiment;

END;
GO
