#!/usr/bin/env python
# coding: utf-8

# ## NB_Silver_To_Gold_Dimensions
# 
# null

# In[2]:


# ==========================================================
# Notebook : NB_Silver_To_Gold_Dimensions
# Purpose  : Load Gold Dimension Tables
# Layer    : Gold Warehouse
# ==========================================================

from pyspark.sql import DataFrame
from pyspark.sql.functions import *
from pyspark.sql.window import Window

# ----------------------------------------------------------
# Configuration
# ----------------------------------------------------------

SILVER_SCHEMA = "Silver"

GOLD_SCHEMA = "Dimensions"

# ----------------------------------------------------------
# Helper Functions
# ----------------------------------------------------------

def read_silver(table_name: str) -> DataFrame:

    return spark.read.table(
        f"{SILVER_SCHEMA}.{table_name}"
    )


def add_surrogate_key(df: DataFrame, key_name: str, order_column: str):

    window = Window.orderBy(order_column)

    return df.withColumn(
        key_name,
        row_number().over(window)
    )


def write_gold(df: DataFrame, table_name: str):

    (
        df.write
        .mode("overwrite")
        .saveAsTable(f"{GOLD_SCHEMA}.{table_name}")
    )

    print(f"✓ {GOLD_SCHEMA}.{table_name} loaded")


def validate(df: DataFrame, table_name: str):

    print(
        f"{table_name:<25}"
        f"{df.count():>10} rows"
    )

# ----------------------------------------------------------
# Read Silver Tables
# ----------------------------------------------------------

customers = read_silver("CustomerFeatures")

products = read_silver("ProductFeatures")

orders = read_silver("Orders")

# ----------------------------------------------------------
# DimCustomer
# ----------------------------------------------------------

dim_customer = (

    customers

    .select(

        "CustomerID",

        "CustomerName",

        "Email",

        "Location",

        "SignupDate"

    )

    .dropDuplicates()

)

dim_customer = add_surrogate_key(

    dim_customer,

    "CustomerKey",

    "CustomerID"

)

dim_customer = (

    dim_customer

    .withColumn(

        "CreatedDate",

        current_timestamp()

    )

    .withColumn(

        "ModifiedDate",

        current_timestamp()

    )

)

write_gold(

    dim_customer,

    "DimCustomer"

)

validate(

    dim_customer,

    "DimCustomer"

)

# ----------------------------------------------------------
# DimProduct
# ----------------------------------------------------------

dim_product = (

    products

    .select(

        "ProductID",

        "ProductName",

        "Category",

        "UnitPrice"

    )

    .dropDuplicates()

)

dim_product = add_surrogate_key(

    dim_product,

    "ProductKey",

    "ProductID"

)

dim_product = (

    dim_product

    .withColumn(

        "CreatedDate",

        current_timestamp()

    )

    .withColumn(

        "ModifiedDate",

        current_timestamp()

    )

)

write_gold(

    dim_product,

    "DimProduct"

)

validate(

    dim_product,

    "DimProduct"

)

# ----------------------------------------------------------
# DimLocation
# ----------------------------------------------------------

dim_location = (

    customers

    .select(

        "Location"

    )

    .distinct()

)

dim_location = add_surrogate_key(

    dim_location,

    "LocationKey",

    "Location"

)

dim_location = (

    dim_location

    .withColumn(

        "CreatedDate",

        current_timestamp()

    )

)

write_gold(

    dim_location,

    "DimLocation"

)

validate(

    dim_location,

    "DimLocation"

)

# ----------------------------------------------------------
# DimPaymentMethod
# ----------------------------------------------------------

dim_payment = (

    orders

    .select(

        "PaymentMethod"

    )

    .distinct()

)

dim_payment = add_surrogate_key(

    dim_payment,

    "PaymentMethodKey",

    "PaymentMethod"

)

dim_payment = (

    dim_payment

    .withColumn(

        "CreatedDate",

        current_timestamp()

    )

)

write_gold(

    dim_payment,

    "DimPaymentMethod"

)

validate(

    dim_payment,

    "DimPaymentMethod"

)

# ----------------------------------------------------------
# DimDate
# ----------------------------------------------------------

dim_date = (

    orders

    .select(

        to_date("OrderDate").alias("CalendarDate")

    )

    .distinct()

)

dim_date = (

    dim_date

    .withColumn(

        "DateKey",

        date_format(

            "CalendarDate",

            "yyyyMMdd"

        ).cast("int")

    )

    .withColumn(

        "DayNumber",

        dayofmonth("CalendarDate")

    )

    .withColumn(

        "MonthNumber",

        month("CalendarDate")

    )

    .withColumn(

        "MonthName",

        date_format(

            "CalendarDate",

            "MMMM"

        )

    )

    .withColumn(

        "QuarterNumber",

        quarter("CalendarDate")

    )

    .withColumn(

        "YearNumber",

        year("CalendarDate")

    )

)

write_gold(

    dim_date,

    "DimDate"

)

validate(

    dim_date,

    "DimDate"

)

# ----------------------------------------------------------
# Summary
# ----------------------------------------------------------

print("=" * 60)

print("SILVER TO GOLD DIMENSIONS SUMMARY")

print("=" * 60)

validate(dim_customer, "DimCustomer")

validate(dim_product, "DimProduct")

validate(dim_location, "DimLocation")

validate(dim_payment, "DimPaymentMethod")

validate(dim_date, "DimDate")

