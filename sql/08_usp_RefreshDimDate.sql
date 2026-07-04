CREATE OR ALTER PROCEDURE Reporting.usp_RefreshDimDate
AS
BEGIN

    SET NOCOUNT ON;

    TRUNCATE TABLE Dimensions.DimDate;

    INSERT INTO Dimensions.DimDate
    (
        CalendarDate,
        DayNumber,
        MonthNumber,
        MonthName,
        QuarterNumber,
        YearNumber
    )

    SELECT DISTINCT

        CAST(OrderDate AS DATE),

        DAY(OrderDate),

        MONTH(OrderDate),

        DATENAME(MONTH, OrderDate),

        DATEPART(QUARTER, OrderDate),

        YEAR(OrderDate)

    FROM Facts.FactSales

    WHERE OrderDate IS NOT NULL;

END;
GO
