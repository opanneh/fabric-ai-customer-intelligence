#!/usr/bin/env python
# coding: utf-8

# ## NB_Bronze_To_Silver
# 
# null

# In[1]:


# ==========================================================
# Notebook : NB_Bronze_To_Silver
# Purpose  : Clean, validate and standardize Bronze data
# Layer    : Silver
# ==========================================================

from pyspark.sql import DataFrame
from pyspark.sql.functions import *

# ----------------------------------------------------------
# Configuration
# ----------------------------------------------------------

BRONZE_SCHEMA = "Bronze"

SILVER_SCHEMA = "Silver"

# ----------------------------------------------------------
# Helper Functions
# ----------------------------------------------------------

def read_bronze(table_name: str) -> DataFrame:
    """
    Read Bronze table.
    """

    return spark.read.table(
        f"{BRONZE_SCHEMA}.{table_name}"
    )


def write_silver(df: DataFrame, table_name: str):
    """
    Save dataframe to Silver.
    """

    (
        df.write
        .mode("overwrite")
        .format("delta")
        .saveAsTable(f"{SILVER_SCHEMA}.{table_name}")
    )

    print(f"✓ Silver.{table_name} created")


def trim_string_columns(df: DataFrame) -> DataFrame:
    """
    Trim all string columns.
    """

    for column_name, column_type in df.dtypes:

        if column_type == "string":

            df = df.withColumn(
                column_name,
                trim(col(column_name))
            )

    return df


def uppercase_ids(df: DataFrame) -> DataFrame:
    """
    Convert all ID columns to uppercase.
    """

    for column_name in df.columns:

        if column_name.upper().endswith("ID"):

            df = df.withColumn(
                column_name,
                upper(col(column_name))
            )

    return df


def lowercase_email(df: DataFrame) -> DataFrame:
    """
    Convert email addresses to lowercase.
    """

    if "Email" in df.columns:

        df = df.withColumn(
            "Email",
            lower(col("Email"))
        )

    return df


def remove_duplicates(df: DataFrame, keys):

    if isinstance(keys, str):
        keys = [keys]

    return df.dropDuplicates(keys)


def validate(before: int, after: int, table_name: str):

    print(
        f"{table_name:<20}"
        f"{before:>8}"
        f"{after:>10}"
        f"{before-after:>10}"
    )

# ----------------------------------------------------------
# Customers
# ----------------------------------------------------------

customers = read_bronze("Customers")

before = customers.count()

customers = (
    customers
    .transform(trim_string_columns)
    .transform(uppercase_ids)
    .transform(lowercase_email)
)

customers = remove_duplicates(
    customers,
    "CustomerID"
)

customers = customers.filter(
    col("CustomerID").isNotNull()
)

after = customers.count()

write_silver(
    customers,
    "Customers"
)

# ----------------------------------------------------------
# Products
# ----------------------------------------------------------

products = read_bronze("Products")

before_products = products.count()

products = (
    products
    .transform(trim_string_columns)
    .transform(uppercase_ids)
)

products = products.filter(
    col("UnitPrice") > 0
)

products = products.filter(
    col("Stock") >= 0
)

products = remove_duplicates(
    products,
    "ProductID"
)

after_products = products.count()

write_silver(
    products,
    "Products"
)

# ----------------------------------------------------------
# Orders
# ----------------------------------------------------------

orders = read_bronze("Orders")

before_orders = orders.count()

orders = (
    orders
    .transform(trim_string_columns)
    .transform(uppercase_ids)
)

orders = orders.filter(
    col("Quantity") > 0
)

orders = orders.filter(
    col("TotalAmount") > 0
)

orders = remove_duplicates(
    orders,
    "OrderID"
)

after_orders = orders.count()

write_silver(
    orders,
    "Orders"
)

# ----------------------------------------------------------
# Reviews
# ----------------------------------------------------------

reviews = read_bronze("Reviews")

before_reviews = reviews.count()

reviews = (
    reviews
    .transform(trim_string_columns)
)

reviews = reviews.filter(
    col("rating").between(1,5)
)

reviews = reviews.filter(
    col("review_text").isNotNull()
)

reviews = remove_duplicates(
    reviews,
    ["customer_id","product_id","timestamp"]
)

after_reviews = reviews.count()

write_silver(
    reviews,
    "Reviews"
)

# ----------------------------------------------------------
# Social Media
# ----------------------------------------------------------

social = read_bronze("SocialMedia")

before_social = social.count()

social = (
    social
    .transform(trim_string_columns)
)

social = social.filter(
    col("content").isNotNull()
)

social = remove_duplicates(
    social,
    ["platform","timestamp","content"]
)

after_social = social.count()

write_silver(
    social,
    "SocialMedia"
)

# ----------------------------------------------------------
# Web Logs
# ----------------------------------------------------------

web = read_bronze("WebLogs")

before_web = web.count()

web = (
    web
    .transform(trim_string_columns)
)

web = remove_duplicates(
    web,
    ["user_id","timestamp","page","action"]
)

after_web = web.count()

write_silver(
    web,
    "WebLogs"
)

# ----------------------------------------------------------
# Validation Summary
# ----------------------------------------------------------

print("=" * 75)
print("BRONZE TO SILVER SUMMARY")
print("=" * 75)

print(
    f"{'Table':<20}"
    f"{'Before':>8}"
    f"{'After':>10}"
    f"{'Removed':>10}"
)

print("-" * 75)

validate(before, after, "Customers")
validate(before_products, after_products, "Products")
validate(before_orders, after_orders, "Orders")
validate(before_reviews, after_reviews, "Reviews")
validate(before_social, after_social, "SocialMedia")
validate(before_web, after_web, "WebLogs")

print("=" * 75)

